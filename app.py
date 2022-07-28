from fpdf import FPDF; import requests

def generate(*args, **kwargs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.output('output.pdf', 'F')
    r = requests.get('https://mrashleyball.github.io/pd-gen/output.pdf')
    with open('output.pdf', 'wb') as f:
        f.write(r.content)