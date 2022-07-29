from fpdf import FPDF
import io
from js import document, window, Uint8Array, File
# from datetime import datetime

def generate(*args, **kwargs):
    # JS grabs id strings value, stores it
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    date = document.getElementById('date').value
    time = document.getElementById('time').value
    event = document.getElementById('event').value

    # if str(time).isalpha():
    #     notification = document.getElementById('notification')
    #     notification.setAttribute('text', 'Time contains non numeric value.')

    if not fname == '' and not lname == '' and not time == '' and not event == '':
        pdf = FPDF(orientation='landscape')
        pdf.add_page()
        pdf.set_font('helvetica', size=12)
        pdf.cell(txt=f'This certificate is for {fname} {lname}.')
        pdf.cell(txt=f'For attending {event} on {date}.')
        pdf.cell(txt=f'{time} hours')

        my_stream = io.BytesIO()

        pdf.output(my_stream)

        pdf_file = File.new([Uint8Array.new(my_stream.getvalue())], 'hello_world.pdf', {'type': 'application/pdf'})

        url = window.URL.createObjectURL(pdf_file)

        link = document.getElementById('download_button')
        link.setAttribute('download', 'certificate.pdf')
        link.setAttribute('href', url)
        link.setAttribute('text', 'Download')
        link.setAttribute('class', 'button is-success')