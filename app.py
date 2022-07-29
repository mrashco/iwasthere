from fpdf import FPDF
import io
from js import document, window, Uint8Array, File
# from datetime import datetime

def generate(*args, **kwargs):
    # JS grabs id strings value, stores it
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    date = document.getElementById('date').value
    email = document.getElementById('email').value
    event = document.getElementById('event').value

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    pdf.cell(txt=f'{fname}, {lname}, {date}, {email}, {event}')

    my_stream = io.BytesIO()

    pdf.output(my_stream)

    pdf_file = File.new([Uint8Array.new(my_stream.getvalue())], 'hello_world.pdf', {'type': 'application/pdf'})

    url = window.URL.createObjectURL(pdf_file)

    link = document.createElement('a')
    link.download = 'certificate.pdf'
    link.href = url
    link.text = 'Download PDF'
    _ = document.body.appendChild(link)