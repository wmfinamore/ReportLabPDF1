from django.shortcuts import render
from django.http.response import FileResponse
from reportingApp.reportlab.program import CreatePDF


def index(request):
    return render(request, 'reportingApp/index.html')

def genPDF(request):
    
    values = request.POST
    
    filename = values.get('fname', 'example.pdf')
    pagesize = values.get('pagesize', 'A4')
    orientation = values.get('orientation', 'landscape')
    userpass = values.get('userpass', '')
    ownerpass = values.get('ownerpass', '')
    
    buffer = CreatePDF(
        orientation=orientation,
        size=pagesize,
        userPass=userpass,
        ownerPass=ownerpass
    )
    
    return FileResponse(
        buffer,
        as_attachment = True,
        filename = filename
    )
