from fpdf import FPDF


class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return bill.amount * weight


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF()
        pdf.add_page()

        pdf.image("./files/house.png", w=30, h=30)

        # Set font for the report
        pdf.set_font("Arial", size=12)

        # Add title
        pdf.set_font("Arial", style='B', size=16)
        pdf.cell(200, 10, txt="Expense Report", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="-----------------------------------", ln=True, align="C")
        pdf.ln(10)

        # Add bill details
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(200, 10, txt=f"Period: {bill.period}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Total Amount: {bill.amount} units", ln=True, align="L")
        pdf.ln(10)

        # Add payment details
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(200, 10, txt="Payment Details:", ln=True, align="L")
        pdf.cell(200, 10, txt=f"{flatmate1.name} pays: {round(flatmate1.pays(bill, flatmate2), 3)} units", ln=True,
                 align="L")
        pdf.cell(200, 10, txt=f"{flatmate2.name} pays: {round(flatmate2.pays(bill, flatmate1), 3)} units", ln=True,
                 align="L")

        # Save PDF
        pdf.output(self.filename)


the_bill = Bill(amount=121, period="March 2021")
john = Flatmate(name='John', days_in_house=15)
marry = Flatmate(name='Marry', days_in_house=20)

pdf_report = PdfReport(filename="expense_report.pdf")
pdf_report.generate(john, marry, the_bill)
