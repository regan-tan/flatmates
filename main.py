from fpdf import FPDF
import webbrowser

class Bill:

    """
    Object that contains data about a bill, such as 
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in the flat and
    pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

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

        pdf.output(self.filename)

        # Automatically open web browser to view generated pdf flatmate bill report
        webbrowser.open(self.filename)

bill = Bill(amount = 1200, period = "August 2021")
john = Flatmate(name="John", days_in_house=20)
kate = Flatmate(name="Kate", days_in_house=31)

print("John.pays: ", john.pays(bill=bill, flatmate2=kate))
print("Kate.pays: ", kate.pays(bill=bill, flatmate2=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=kate, bill=bill)