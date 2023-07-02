Flatmates Bill Documentation
This code is a simple implementation to calculate and generate a bill for flatmates living together. It includes three classes: Bill, Flatmate, and PdfReport. Below is a detailed explanation of each class and its purpose.

**Bill Class**
The Bill class represents a bill object and contains information about the total amount and period of the bill. It has the following attributes and methods:

Attributes
amount: The total amount of the bill.
period: The period for which the bill is generated.
Methods
__init__(self, amount, period): The constructor method initializes the Bill object with the provided amount and period.


**Flatmate Class**
The Flatmate class represents a person who lives in the flat and pays a share of the bill. It has the following attributes and methods:

Attributes
name: The name of the flatmate.
days_in_house: The number of days the flatmate stayed in the house during the billing period.
Methods
__init__(self, name, days_in_house): The constructor method initializes the Flatmate object with the provided name and days_in_house.
pays(self, bill, flatmate2): This method calculates and returns the amount that the flatmate needs to pay based on their share of the bill. It takes the bill object and the other flatmate2 object as parameters.


**PdfReport Class**
The PdfReport class creates a PDF file that contains data about the flatmates and their bill amounts for a specific period. It has the following attributes and methods:

Attributes
filename: The name of the PDF file to be generated.
Methods
__init__(self, filename): The constructor method initializes the PdfReport object with the provided filename.
generate(self, flatmate1, flatmate2, bill): This method generates the PDF report with the given flatmates and bill details. It takes the flatmate1 and flatmate2 objects, along with the bill object, as parameters.
It creates an instance of the FPDF class from the fpdf module.
Adds a page to the PDF.
Sets the font and inserts the title.
Inserts the period label and its value.
Inserts the name and bill amount for the first flatmate.
Outputs the PDF with the specified filename.


**Execution**
The code after the class definitions demonstrates how to use the classes to calculate the bill and generate a PDF report. It does the following:

Creates an instance of the Bill class with an amount of 1200 and a period of "August 2021".
Creates two instances of the Flatmate class: john and kate.
Prints the amount that John and Kate need to pay based on their share of the bill using the pays method of the Flatmate class.
Creates an instance of the PdfReport class with a filename of "Report1.pdf".
Generates the PDF report using the generate method of the PdfReport class, providing the john, kate, and bill objects as parameters.
Make sure to have the fpdf module installed in your Python environment before running this code.
