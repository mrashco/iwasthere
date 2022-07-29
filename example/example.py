from fpdf import FPDF
import io
from js import document, window, Uint8Array, File

#Some very basic PDF creation, using the example on the fpdf documentation
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt='hello world')

#Create a BytesIO object (acts like a file in memory) to hold PDF output
my_stream = io.BytesIO()

#Write bytes of PDF to BytesIO object
pdf.output(my_stream)

#Create new File object (see JS File API).
#Casting to Uint8Array necessary to prevent my_stream's value from being interpretted
#as one giant number
pdf_file = File.new([Uint8Array.new(my_stream.getvalue())], 'hello_world.pdf', {'type': 'application/pdf'})

#Get a URL to reference this in-memory file object
url = window.URL.createObjectURL(pdf_file)

#Create link (wihtout placing it in DOM) with download attribute, point it at our URL, and click it
link = document.createElement('a')
link.download = 'hello_world.pdf'
link.href = url
link.text = 'Download PDF'
_ = document.body.appendChild(link) #assignment prevents Pyodide/pyscript from printing return value