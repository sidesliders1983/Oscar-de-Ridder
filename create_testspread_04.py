"""Build an exact A3 reading proof with separately typeset vector text."""
from pathlib import Path
import re,json
from xml.sax.saxutils import escape
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT=Path(__file__).parent
ART=ROOT/'artwork/book-3/concepts/spreads/spread-04-test-a3-v001.png'
OUT=ROOT/'output/pdf/boek-3-testspread-04-a3-v001.pdf'
QA=ROOT/'tmp/pdfs/testspread-04-v001'
QA.mkdir(parents=True,exist_ok=True)
OUT.parent.mkdir(parents=True,exist_ok=True)
src=(ROOT/'storyboard/book-3/visual-storyboard-v003.md').read_text(encoding='utf-8')
body=re.search(r'^### 04 — .*?\n(.*?)(?=^## )',src,re.S|re.M).group(1)
left,right=body.split('**Rechts**')
texts=[left.split('**Links**')[1],right]
blocks=[[line.rstrip('\\').strip() for line in text.strip().splitlines() if line.strip()] for text in texts]
pdfmetrics.registerFont(TTFont('Reading','C:/Windows/Fonts/segoepr.ttf'))
pdfmetrics.registerFont(TTFont('ReadingBold','C:/Windows/Fonts/segoeprb.ttf'))
pdfmetrics.registerFontFamily('Reading',normal='Reading',bold='ReadingBold')
W,H=420*mm,297*mm
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('Gebulder in de Bergen - testspread 04')
c.setAuthor('Oscar de Ridder')
c.drawImage(str(ART),0,0,width=W,height=H)
style=ParagraphStyle('Story',fontName='Reading',fontSize=16,leading=25,textColor='#302919',alignment=1)
boxes=[]
for side,lines in enumerate(blocks):
    x=(30 if side==0 else 240)*mm
    width=150*mm
    y=80*mm
    for line in lines:
        txt=escape(line).replace('PLOENS!','<font color="#9C3B22"><b>PLOENS!</b></font>')
        p=Paragraph(txt,style);_,height=p.wrap(width,200)
        y-=height
        assert y>15*mm, f'Text outside safe area: {y}'
        p.drawOn(c,x,y)
        boxes.append([x,y,width,height]);y-=6
c.showPage();c.save()
r=PdfReader(OUT)
assert len(r.pages)==1
assert abs(float(r.pages[0].mediabox.width)-W)<.01
assert abs(float(r.pages[0].mediabox.height)-H)<.01
extracted=r.pages[0].extract_text()
for line in blocks[0]+blocks[1]:
    assert ' '.join(line.split()) in ' '.join(extracted.split()),line
doc=pdfium.PdfDocument(str(OUT))
doc[0].render(scale=1.5).to_pil().save(QA/'preview.png')
iw,ih=Image.open(ART).size
meta={'page_mm':[420,297],'native_image_px':[iw,ih],'effective_ppi':round(iw/(420/25.4),1),'text':'embedded vector text, Segoe Print 16pt','source':'storyboard/book-3/visual-storyboard-v003.md scene04','status':'testspread concept','text_boxes_pt':boxes}
(QA/'validation.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print(json.dumps(meta,indent=2))
print(OUT)
