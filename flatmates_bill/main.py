from flat import Bill, Flatmate
from flatmates_bill.report import PdfReport

amount = float(input("Hey user, enter the total bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period {period}? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period {period}? "))

bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", flatmate1.pays(bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport(filename=f'{bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, bill)