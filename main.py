from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
data = pd.read_csv('topics.csv')

for index, rows in data.iterrows():
    pdf.add_page()
    for i in range(rows['Pages']):
        pdf.add_page()
    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1, border=0)
    pdf.line(10, 20, 200, 20)
    #pdf.footer(rows['Topic'])


pdf.output('output.pdf')
