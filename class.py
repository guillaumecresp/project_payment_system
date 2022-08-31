class client:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
class User(client):
    is_User = True

class payment:
    def __init__(self, card_number, cvv, expiry_date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
    def display(self):
        print("Card Number: ", self.card_number)
        print("CVV: ", self.cvv)
        print("Expiry Date: ", self.expiry_date)

class Bank(payment):
    is_Bank = True
    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number
    def display(self):
        print("Bank Name: ", self.bank_name)
        print("Account Number: ", self.account_number)