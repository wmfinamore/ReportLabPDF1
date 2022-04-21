from turtle import fillcolor
from reportlab.pdfgen import canvas
from reportlab.platypus import Table

from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib import colors


def getFiveStars():
    drawing = Drawing(0, 0)
    
    drawing.add(Rect(0, 0, 100, 50,
                     fillColor='orange',
                     strokeColor = colors.blue,
                     strokeWidth = 3
                     ))
    
    return drawing

if __name__ == '__main__':
    pdf = canvas.Canvas('starTest.pdf')
    
    drawing = getFiveStars()
    tab = Table([[drawing]], 250, 150)
    
    tab.setStyle([
        ('GRID', (0,0), (-1,-1), 0.1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    
    tab.wrapOn(pdf, 0, 0)
    tab.drawOn(pdf, 100, 600)
    
    pdf.save()
    