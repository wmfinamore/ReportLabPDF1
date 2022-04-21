from turtle import fillcolor
from reportlab.pdfgen import canvas
from reportlab.platypus import Table

from reportlab.graphics.shapes import Drawing, Rect, Polygon, Group
from reportlab.lib import colors

from math import sin, cos, pi


def _getStar():
    angle = 90
    radius1 = 5
    radius2 = radius1*sin(18*(pi/180.0))/cos(36*(pi/180.0))
    
    points = []
    
    for i in range(5):
        for radius in [radius1, radius2]:
            theta = angle * (pi / 180.0)
            points.append(radius*cos(theta)) # x pos
            points.append(radius*sin(theta)) # y pos
            
            angle = angle + 36
    polygon = Polygon(
        points,
        fillColor = colors.burlywood,
        strokeColor = colors.darkgoldenrod,
        strokeWidth = 0.5
    )
    return polygon

def getFiveStars():
    drawing = Drawing(0, 0)

    polygon = _getStar()
    
    for x in range(-2, 3):
        group = Group()
        group.add(polygon)
        group.translate(x * 15, 10)
        
        drawing.add(group)
    
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
    