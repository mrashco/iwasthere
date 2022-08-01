from fpdf import FPDF
import io
from pyodide.http import pyfetch
from js import document, window, Uint8Array, File
from datetime import datetime

async def generate(*args, **kwargs):
    # JS grabs id strings value, stores it
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    date = document.getElementById('date').value
    hours = document.getElementById('hours').value
    event = document.getElementById('event').value

    if not fname == '' and not lname == '' and not hours == '' and not event == '':
        pdf = FPDF(orientation='landscape')
        pdf.add_page()
        
        # global image_io
        # image_io = getImage()
        # pdf.image(image_io, 0, 0, 297, 210)

        image_url = 'cert.png'
        response = await pyfetch(url=image_url, method='GET')
        image_io = io.BytesIO(await response.bytes())
        pdf.image(image_io, 0, 0, 297, 210)
        
        pdf.set_font('helvetica', size=24)
        pdf.set_xy(35, 70)
        pdf.multi_cell(w=80, h=20, txt='Awarded to:\nAttendance of:\nDate:\nAmount of hours:')
        pdf.set_xy(115, 70)
        pdf.multi_cell(w=80, h=20, txt=f'{fname} {lname}\n{event}\n{date}\n{hours}')

        my_stream = io.BytesIO()

        pdf.output(my_stream)

        pdf_file = File.new([Uint8Array.new(my_stream.getvalue())], 'hello_world.pdf', {'type': 'application/pdf'})

        url = window.URL.createObjectURL(pdf_file)
        time_now = getTimeNow()
        
        # Remove spaces and return with dashes for filename
        fname, lname, event = rmvSpaces(fname), rmvSpaces(lname), rmvSpaces(event)
        link = document.getElementById('generate')
        link.setAttribute('download', f'iwasthere-{fname}-{lname}-{event}-{time_now}.pdf'.lower())
        link.setAttribute('href', url)
        link.setAttribute('text', 'Download')
        # link.setAttribute('class', 'button is-success')

def getTimeNow():
    now = datetime.now()
    return now.strftime(r'%d-%m-%Y-%H-%M-%S')

def rmvSpaces(name):
    new_name = ''
    for char in name:
        if char == ' ':
            char = '-'
        new_name += char
    return new_name

# async def getImage():
#         image_url = 'cert.png'
#         response = await pyfetch(url=image_url, method='GET')
#         # global image_io
#         return io.BytesIO(await response.bytes())