from reportlab.lib import colors
from reportlab.platypus import Table

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
    
    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LINEBELOW', (1,0), (1,1), 5, color)
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
    return 'ABOUT'