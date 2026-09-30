"""Create a 16-page A3 landscape concept proof with separate vector text."""
from pathlib import Path
import re
from docx import Document
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from pypdf import PdfReader
import pypdfium2 as pdfium
import json

ROOT=Path(__file__).parent
ART=ROOT/'artwork/book-3/concepts/spreads'
OUT=ROOT/'output/pdf/boek-3-testspreads-a3-v001.pdf'
QA=ROOT/'tmp/pdfs/book-3-testspreads-v001'
QA.mkdir(parents=True,exist_ok=True)
OUT.parent.mkdir(parents=True,exist_ok=True)
W,H=420*mm,297*mm
TEXT_H=98*mm
DOC=ROOT/'storyboard/book-3/voorleestekst-v001.docx'

def extract_spreads():
    doc=Document(DOC)
    spreads={}
    current=None; side=None
    for para in doc.paragraphs:
        text=para.text.strip()
        if para.style.name=='Heading 1' and len(text)>=2 and text[:2].isdigit():
            num=int(text[:2]); current={'title':text[5:], 'left':[], 'right':[]}; spreads[num]=current; side=None
        elif current and para.style.name=='Heading 3' and text in ('Links','Rechts'):
            side='left' if text=='Links' else 'right'
        elif current and side and text and para.style.name not in ('Heading 1','Heading 3'):
            line=text.rstrip('\\').strip()
            if line:
                # Apply the latest explicit author corrections to this typeset proof.
                line=line.replace('KWWAAAAAAAK.','GRAAAAUW!')
                line=re.sub(r'GRA+UW!', 'GRAAAAUW!', line)
                line=line.replace('Boos kwam de draak overeind.','Boos ging de draak op zijn achterpoten staan.')
                if current['title'].startswith('Patrick?!') and line.startswith('‘KWWAAAAAAAK.'):
                    line='‘GRAAAAUW!’ bulderde Patrick de brulkikker.'
                current[side].append(line)
    if sorted(spreads)!=list(range(1,17)):
        raise ValueError(f'Expected 16 spreads, found {sorted(spreads)}')
    return spreads

def flowers(c,x,y,scale=1):
    # Small corner sprigs; each flower is about 7 mm across.
    c.saveState(); c.setLineWidth(.65); c.setStrokeColorRGB(.30,.40,.24)
    c.setFillColorRGB(.38,.52,.31)
    path=c.beginPath(); path.moveTo(x,y); path.curveTo(x+2*mm,y+4*mm,x-1*mm,y+8*mm,x+2*mm,y+12*mm); c.drawPath(path)
    c.ellipse(x+1*mm,y+4*mm,x+4*mm,y+5.3*mm,fill=1,stroke=0)
    c.ellipse(x-0.8*mm,y+8*mm,x+2*mm,y+9.3*mm,fill=1,stroke=0)
    colors=[(0.67,.40,.31),(.81,.61,.26),(.58,.48,.68)]
    for dx,dy,col in [(0,14,colors[0]),(4,17,colors[1]),(-3,19,colors[2])]:
        xx=x+dx*mm; yy=y+dy*mm; c.setFillColorRGB(*col)
        for a in range(5):
            import math
            ang=2*math.pi*a/5
            px=xx+math.cos(ang)*1.45*mm; py=yy+math.sin(ang)*1.45*mm
            c.circle(px,py,0.9*mm,fill=1,stroke=0)
        c.setFillColorRGB(.84,.68,.33); c.circle(xx,yy,.75*mm,fill=1,stroke=0)
    c.restoreState()

def draw_block(c,lines,x,y,width):
    style=ParagraphStyle('read',fontName='Read',fontSize=15,leading=21.5,textColor='#332B1D',alignment=1,spaceAfter=5)
    for line in lines:
        safe=escape(line)
        for word,color in [('PLOENS!','#A34427'),('TING!','#A34427'),('GRAAAAAUW!','#A34427'),('GRAAAAUW!','#A34427'),('KWWAAAAAAAK.','#A34427'),('BOEM.','#A34427'),('FLAP.','#A34427')]:
            safe=safe.replace(word,f'<font color="{color}"><b>{word}</b></font>')
        p=Paragraph(safe,style)
        _,h=p.wrap(width,1000)
        y-=h
        if y < 6*mm:
            raise ValueError(f'Text overflows column: {line}')
        p.drawOn(c,x,y)
        y-=style.spaceAfter

def main():
    pdfmetrics.registerFont(TTFont('Read','C:/Windows/Fonts/segoepr.ttf'))
    pdfmetrics.registerFont(TTFont('ReadBold','C:/Windows/Fonts/segoeprb.ttf'))
    pdfmetrics.registerFontFamily('Read',normal='Read',bold='ReadBold')
    spreads=extract_spreads()
    c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
    c.setTitle('Gebulder in de Bergen — A3 testspreads')
    c.setAuthor('Oscar de Ridder')
    checks=[]
    for n in range(1,17):
        art=ART/f'spread-{n:02d}-v001.png'
        if n==4:
            art=ART/'spread-04-test-a3-v001.png'
        elif n==5 and (ART/'spread-05-v002.png').exists():
            art=ART/'spread-05-v002.png'
        if not art.exists():
            fallback=ART/f'spread-{n:02d}-storyboard-crop-v003.jpg'
            if n not in (14,15,16) or not fallback.exists():
                raise FileNotFoundError(f'Missing illustration for scene {n}: {art}')
            c.setFillColorRGB(.975,.922,.805); c.rect(0,0,W,H,fill=1,stroke=0)
            c.drawImage(str(fallback),0,TEXT_H,width=W,height=H-TEXT_H)
        else:
            c.drawImage(str(art),0,0,width=W,height=H,mask='auto')
        c.setFillColorRGB(.975,.922,.805)
        c.rect(0,0,W,TEXT_H,fill=1,stroke=0)
        flowers(c,8*mm,3*mm); flowers(c,W-10*mm,3*mm)
        draw_block(c,spreads[n]['left'],25*mm,89*mm,165*mm)
        draw_block(c,spreads[n]['right'],230*mm,89*mm,165*mm)
        c.showPage()
        checks.append({'spread':n,'title':spreads[n]['title'],'left_lines':len(spreads[n]['left']),'right_lines':len(spreads[n]['right'])})
    c.save()
    r=PdfReader(OUT)
    assert len(r.pages)==16
    for page in r.pages:
        assert abs(float(page.mediabox.width)-W)<.01 and abs(float(page.mediabox.height)-H)<.01
    alltext='\n'.join(p.extract_text() or '' for p in r.pages)
    assert alltext.count('GRAAAAUW!')>=2  # normalized narration in scenes 14 and 15
    # Contact sheet at readable thumbnail size for visual review.
    d=pdfium.PdfDocument(str(OUT))
    thumbs=[d[i].render(scale=.28).to_pil() for i in range(16)]
    from PIL import Image,ImageOps,ImageDraw
    tw,th=thumbs[0].size; sheet=Image.new('RGB',(tw*4,th*4),(236,226,207))
    for i,img in enumerate(thumbs): sheet.paste(img,((i%4)*tw,(i//4)*th))
    sheet.save(QA/'contact-sheet.jpg',quality=92)
    (QA/'validation.json').write_text(json.dumps({'pages':len(r.pages),'page_mm':[420,297],'text_source':str(DOC.relative_to(ROOT)),'layout':checks},ensure_ascii=False,indent=2),encoding='utf-8')
    print(OUT)

if __name__=='__main__': main()
