from turtle import left
from reportlab.platypus import Table, Image


def genHeaderTable(width, height):
    widthList = [
        width * 0.55, # col 1 - left image
        width * 0.45, # col 2 - right image
        width * 0, # text
    ]
    
    leftImagePath = 'resources\paradiseHotel.jpg'
    leftImageWidth = widthList[0]
    leftImage = Image(leftImagePath, leftImageWidth, height)
    
    rightImagePath = 'resources\logoParadise.png'
    rightImageWidth = widthList[1]
    rightImage = Image(rightImagePath, rightImageWidth, height,
                       kind='proportional')
    
    rightText = 'HOTEL'
    # rightList = [rightImage, rightText]
    
    res = Table([
        [leftImage, rightImage, rightText]
    ],
    widthList, height)
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        
        ('FONTSIZE', (2, 0), (2, 0), 20),
        ('LEFTPADDING', (2, 0), (2, 0), -widthList[1] + 98), # text
        ('BOTTOMPADDING', (2, 0), (2, 0), 40), # text
        
    ])
    
    return res # res = Resultado