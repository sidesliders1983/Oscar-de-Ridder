"""Printable review PDF from current storyboard; original artwork stays intact."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from PIL import Image
import pypdfium2 as pdfium
from pypdf import PdfReader

ROOT = Path(__file__).parent
OUT = ROOT / 'output/pdf/boek-3-storyboard-print-v001.pdf'
QA = ROOT / 'tmp/pdfs/storyboard-print-v001'
OUT.parent.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold', 'C:/Windows/Fonts/arialbd.ttf'))
source = (ROOT / 'storyboard/book-3/voorleestekst-v002.md').read_text(encoding='utf-8')
parts = re.split(r'^## (\d{2}) — (.+)$', source, flags=re.M)
boards = [
    ('board-01-04-v006.png', (84, 463), (548, 932)),
    ('board-05-08-v005.png', (90, 430), (552, 899)),
    ('board-09-12-v005.png', (92, 439), (556, 913)),
    ('board-13-16-v006.png', (80, 484), (555, 951)),
]
W,H = landscape(A4)
c = canvas.Canvas(str(OUT), pagesize=(W,H))
c.setTitle('Gebulder in de Bergen - storyboard met voorleestekst')
c.setAuthor('Oscar de Ridder')
style = ParagraphStyle('Reading', fontName='Arial', fontSize=13, leading=18, spaceAfter=3)
for i in range(1,len(parts),3):
    nr,title,body = parts[i:i+3]
    n=int(nr)-1
    halves=body.split('**Rechts**')
    texts=[halves[0].split('**Links**')[1], halves[1]]
    c.setFillColorRGB(.18,.18,.18)
    c.setFont('ArialBold',15)
    c.drawString(34,H-31,f'{nr}  {title}')
    c.setFont('Arial',9)
    c.drawRightString(W-34,H-29,'Gebulder in de Bergen | Lees- en kijkversie')
    filename,top,bottom=boards[n//4]
    path=ROOT/'artwork/book-3/concepts/storyboard'/filename
    iw,ih=Image.open(path).size
    row=top if n%4<2 else bottom
    # Clip the existing contact sheet directly on the PDF canvas; no new art.
    x0,x1=((16,758) if n%2==0 else (778,1519))
    y0,y1=row
    sx,sy=iw/1536,ih/1024
    x0*=sx; x1*=sx; y0*=sy; y1*=sy
    regionw,regionh=x1-x0,y1-y0
    area_x,area_y,area_w,area_h=34,239,W-68,H-289
    scale=min(area_w/regionw,area_h/regionh)
    rw,rh=regionw*scale,regionh*scale
    px=area_x+(area_w-rw)/2; py=area_y+(area_h-rh)/2
    c.saveState()
    clip=c.beginPath(); clip.rect(px,py,rw,rh); c.clipPath(clip,stroke=0)
    c.drawImage(str(path),px-x0*scale,py-(ih-y1)*scale,width=iw*scale,height=ih*scale)
    c.restoreState()
    colw=(W-100)/2
    for side,txt in enumerate(texts):
        x=34+side*(colw+32)
        c.setFillColorRGB(.4,.4,.4);c.setFont('ArialBold',9)
        c.drawString(x,220,'LINKS' if side==0 else 'RECHTS')
        y=203
        for line in txt.strip().splitlines():
            line=line.rstrip('\\').strip()
            if not line: continue
            p=Paragraph(escape(line),style)
            _,ph=p.wrap(colw,180)
            y-=ph
            if y<39: raise ValueError(f'Text overflow in scene {nr}')
            p.drawOn(c,x,y); y-=3
    c.setFillColorRGB(.4,.4,.4);c.setFont('Arial',8)
    c.drawString(34,20,'Concept storyboard • Tekstcorrecties verwerkt • 30 september 2026')
    c.drawRightString(W-34,20,f'{n+1} / 16')
    c.showPage()
c.save()
doc=pdfium.PdfDocument(str(OUT))
assert len(doc)==16
assert 'achterpoten staan' in PdfReader(OUT).pages[8].extract_text()
for n,page in enumerate(doc):
    page.render(scale=1).to_pil().save(QA/f'page-{n+1:02}.png')
# Four review montages from rendered pages, not modified artwork.
for b in range(4):
    sheet=Image.new('RGB',(1684,1192),'white')
    for j in range(4):
        img=Image.open(QA/f'page-{b*4+j+1:02}.png')
        sheet.paste(img,((j%2)*842,(j//2)*596))
    sheet.save(QA/f'review-{b+1}.png')
print(f'{OUT}\n16 pages, no text overflow; scene 09 correction verified.')
