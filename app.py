from fpdf import FPDF
import io
from js import document, window, Uint8Array, File
from datetime import datetime

def generate(*args, **kwargs):
    # JS grabs id strings value, stores it
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    date = document.getElementById('date').value
    hours = document.getElementById('hours').value
    event = document.getElementById('event').value

    if not fname == '' and not lname == '' and not hours == '' and not event == '':
        pdf = FPDF(orientation='landscape')
        # cert_image = open("cert.png", "rb", buffering=0)
        pdf.add_page()
        # pdf.image(cert_image)
        pdf.set_font('helvetica', size=12)
        pdf.cell(txt=f'This certificate is for {fname} {lname}.')
        pdf.cell(txt=f'For attending {event} on {date}.')
        pdf.cell(txt=f'{hours} hours')

        my_stream = io.BytesIO()

        pdf.output(my_stream)

        pdf_file = File.new([Uint8Array.new(my_stream.getvalue())], 'hello_world.pdf', {'type': 'application/pdf'})

        url = window.URL.createObjectURL(pdf_file)
        time_now = getTimeNow()
        
        # Remove spaces and return with dashes for filename
        fname, lname, event = removeSpaces(fname), removeSpaces(lname), removeSpaces(event)
        link = document.getElementById('generate')
        link.setAttribute('download', f'iwasthere-{fname}-{lname}-{event}-{time_now}.pdf'.lower())
        link.setAttribute('href', url)
        link.setAttribute('text', 'Download')
        # link.setAttribute('class', 'button is-success')

def getTimeNow():
    now = datetime.now()
    return now.strftime(r'%d-%m-%Y-%H-%M-%S')

def removeSpaces(name):
    new_name = ''
    for char in name:
        if char == ' ':
            char = '-'
        new_name += char
    return new_name
