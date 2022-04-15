from reportlab.lib import colors
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle

def genBodyTable(width, height):
    
    widthList = [
        width * 0.10, #left 'padding'
        width * 0.80, # values
        width * 0.10, # right 'padding'
    ]
    
    heightList = [
        height * 0.10, # offer 0
        height * 0.15, # contacts 1
        height * 0.35, # prices 2
        height * 0.30, # description 3
        height * 0.10, # about 4
        
    ]
    
    res = Table([
        ['', 'Offer', ''],
        ['', _genContactsTable(widthList[1], heightList[1]), ''],
        ['', _genPriceListTable(widthList[1], heightList[2]), ''],
        ['', _genDescriptionParasList(), ''],
        ['', _genAboutTable(widthList[1], heightList[4]), ''],
    ],
        widthList,
        heightList)
    
    color = colors.HexColor('#003363')
    leftPadding = 20
    
    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LINEBELOW', (1,0), (1,1), 1, color),
        ('LINEBELOW', (1,3), (1,3), 1, color),
        
        ('LEFTPADDING', (1, 0), (1,3), leftPadding),
        
        ('FONTSIZE', (1, 0), (1, 0), 30),
        ('BOTTOMPADDING', (1, 0), (1, 0), 30),
        
        ('BOTTOMPADDING', (1, 1), (1, 2), 0),
        
        ('BOTTOMPADDING', (1, 3), (1, 3), 40),
        
        ('BOTTOMPADDING', (1, 4), (1, 4), 0),
        ('LEFTPADDING', (1, 4), (1, 4), 0),
    ])
    
    return res

## Functions for internal tables

def _genContactsTable(width, height):
    return 'CONTACTS'

def _genPriceListTable(width, height):
    return 'PRICES'

def _genDescriptionParasList():
    return 'DESCRIPTION'

def _genAboutTable(width, height):
    widthList = [
        width * 0.20,
        width * 0.80,
    ]
    
    img = Image(
        'resources\logoParadise.png',
        widthList[0],
        height,
        kind='proportional'
    )
    
    para1Style = ParagraphStyle('para1', )
    para1Style.fontSize = 14
    para1Style.spaceAfter = 15
    para1 = Paragraph('Palms Hotels', para1Style)
    
    para2Style = ParagraphStyle('para2', )
    para2Style.fontSize = 8
    para2 = Paragraph('''
    Ever since 2004, Palms Hotel has received accommodation and
    dining guests. The hotel and the restaurants has been run 
    and owned by Dabai SGPS.
    ''', para2Style)
    
    paras = [para1, para2]
    
    res = Table([
        [img, paras, ]
    ],
    widthList,
    height)
    
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        
        ('BOTTOMPADDING',(0, 0), (1, 0), 0),
        
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),
        
    ])
    
    return res