import webbrowser
from fpdf import FPDF
# import os

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates and their bill amounts for the 
    period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add image to pdf
        pdf.image("house.jpeg", w=50, h=50)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size = 16, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert Name and bill amount of first flatmate
        pdf.set_font(family='Times', size = 12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert Name and bill amount of second flatmate
        pdf.set_font(family='Times', size = 12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # os.chdir("files")

        pdf.output(self.filename)

        # Automatically open web browser to view generated pdf flatmate bill report
        webbrowser.open(self.filename)