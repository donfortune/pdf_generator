from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


data = pd.read_csv('topics.csv')
# adding the header
for index, rows in data.iterrows():
    pdf.add_page()

    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1, border=0)
    pdf.line(10, 20, 200, 20)
    #adding footer
    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R', ln=1, border=0)


    for i in range(rows['Pages']):
        pdf.add_page()

        pdf.ln(275)

        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=rows['Topic'], align='R', ln=1, border=0)


pdf.output('output.pdf')
