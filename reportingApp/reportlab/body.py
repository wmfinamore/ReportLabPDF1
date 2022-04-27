from reportlab.lib import colors
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from .utils import BASE_PATH

import csv

from .stars import getFiveStars

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
    
    leftPadding = 20
    tablesWidth = widthList[1]-leftPadding # adjusting tables width
    
    res = Table([
        ['', 'Offer', ''],
        ['', _genContactsTable(tablesWidth, heightList[1]), ''],
        ['', _genPriceListTable(tablesWidth, heightList[2]), ''],
        ['', _genDescriptionParasList(), ''],
        ['', _genAboutTable(widthList[1], heightList[4]), ''],
    ],
        widthList,
        heightList)
    
    color = colors.HexColor('#003363')
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        
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
    widthList = [
        width * 0.30,
        width * 0.30,
        width * 0.20,
        width * 0.20,
    ]
    heightList = [
        height * 0.25,
        height * 0.25,
        height * 0.25,
        height * 0.25,
    ]
    
    dataList = []
    
    # open file and create a lista with contact values
    with open(BASE_PATH / r'resources\tabledata.txt', 'r') as file:
        for line in file:
            if line != '\n':
                dataList.append(line.replace('/n', ''))
    
    # create matrix(list of string lists)
    matrix = [
        ['','','',''],
        ['','','',''],
        ['','','',''],
        ['','','',''],
    ]
    
    # include values of contacts in the matrix
    idx = 0
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            matrix[ridx][cidx] = dataList[idx]
            idx += 1
            
            if idx == len(dataList):
                break
        if idx == len(dataList):
                break
    
    res = Table(matrix, widthList, heightList)
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
        ('RIGHTPADDING', (3, 0), (3, -1), 20),
        
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    
    return res

def _genPriceListTable(width, height):
    
    titleStyle = ParagraphStyle('titleStyle')
    titleStyle.fontSize = 20
    titleStyle.fontName = 'Helvetica-Bold'
    titleStyle.spaceAfter = 15
    
    titlePara = Paragraph('Details', titleStyle)
    
    pricesTable = _genPricesTable(width, height * 0.70)
    
    elementsList = [titlePara, pricesTable]
    
    
    res = Table([
        [elementsList],
    ], width, height)
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        
        
    ])
    
    return res

def _genDescriptionParasList():
    res = []
    
    para1Style = ParagraphStyle('para1d')
    para1Style.fontSize = 10
    para1Style.spaceAfter = 15
    para1Style.textColor = colors.HexColor('#003363')
    para1Style.fontName = 'jetBrainsMonoExtraBold'
    
    para2Style = ParagraphStyle('para2d')
    para2Style.fontSize = 10
    para2Style.fontName = 'jetBrainsMonoRegular'
    
    para1 = Paragraph('''
    Thank you very much for using the services from us at Palms.
    Here at Palms Hotel we have living rooms and well-equipped
    meeting rooms of all sizes with a capacitu from 8 - 300 people,
    so that we will be well prepared for most needs you may have.    
    ''', para1Style)
    para2 = Paragraph('''
    <i>
    <b>Palms Hotel</b> is also known for its cuisine and good service,
    therefore you can feel confident that your needs and desires
    will be ewll taken care of, whether you choose to user our
    beautiful Restaurant Palms or other living rooms,
    we guarantee a <u>good experience with us.</u>
    </i>
    ''', para2Style)
    
    res.append(para1)
    res.append(para2)
    
    return res

def _genAboutTable(width, height):
    
    widthList = [
        width * 0.20,
        width * 0.80,
    ]
    
    img = Image(
        BASE_PATH / 'resources\logoParadise.png',
        widthList[0],
        height,
        kind='proportional'
    )
    
    drawing = getFiveStars()
    
    para1Style = ParagraphStyle('para1', )
    para1Style.fontSize = 14
    para1Style.spaceAfter = 8
    para1 = Paragraph('Palms Hotels', para1Style)
    
    para2Style = ParagraphStyle('para2', )
    para2Style.fontSize = 8
    para2 = Paragraph('''
    Ever since 2004, Palms Hotel has received accommodation and
    dining guests. The hotel and the restaurants has been run 
    and owned by Dabai SGPS.
    ''', para2Style)
    
    imgs = [img, drawing]
    paras = [para1, para2]
    
    res = Table([
        [imgs, paras, ]
    ],
    widthList,
    height)
    
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        
        ('BOTTOMPADDING',(0, 0), (0, 0), height/3), # first column
        ('BOTTOMPADDING',(1, 0), (1, 0), 0), # second column
        
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),
        
    ])
    
    return res

def _genPricesTable(width, height):
    matrix = []
    
    with open(BASE_PATH / r'resources\pricesTable.csv', 'r') as file:
        matrix = list(csv.reader(file))
        
    if len(matrix) < 2 or len(matrix[0]) !=6 :
        return Table(['no data'])
    
    widthList = [
        width * 0.20,
        width * 0.20,
        width * 0.25,
        width * 0.15,
        width * 0.10,
        width * 0.10,
    ]
    
    rowCount = len(matrix)
    
    res = Table(matrix, widthList, height/rowCount )
    
    color = colors.toColor('rgba(0, 115, 153, 0.9)')
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),
        
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        
        ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
        
        ('ALIGN', (1, 1), (2, -1), 'CENTER'),
        
        ('ALIGN', (5, 1), (5, -1), 'RIGHT'),
        
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), ['antiquewhite', 'beige'])
        
    ])
    
    return res