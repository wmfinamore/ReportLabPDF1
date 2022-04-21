from turtle import fillcolor
from reportlab.pdfgen import canvas
from reportlab.platypus import Table

from reportlab.graphics.shapes import Drawing, Rect, Polygon
from reportlab.lib import colors


def _getTriangle(xOffset = 0):
    
    points = []
    
    points.append(0 + xOffset) # x1
    points.append(0) # y1
    
    points.append(15 + xOffset) #x2
    points.append(0) # y2
    
    points.extend([7.5 + xOffset, 10]) # x3 e y3
    
    polygon = Polygon(points,
                      fillColor = colors.burlywood,
                      strokeColor = colors.darkgoldenrod,
                      strokeWidth = 0.5
                      )
    return polygon

def getFiveStars():
    drawing = Drawing(0, 0)

    for x in range(5):
    
        polygon = _getTriangle( x * 15)
        drawing.add(polygon)
    
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
    