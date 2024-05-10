class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house/(self.days_in_house+flatmate.days_in_house)
        return bill.amount*weight


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name='John', days_in_house=5)
marry = Flatmate(name='Marry', days_in_house=10)

print(f'John pays: {john.pays(the_bill, flatmate=marry)}')
print(f'Marry pays: {marry.pays(the_bill, flatmate=john)}')