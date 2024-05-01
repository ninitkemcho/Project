import random
from account_creation import accounts, add_account
ibans = []
history = {}

def menu():
    menu = ["1. Create bank account", "2. Control balance", "3. Transfer money", "4. Account details", "5. Account history", "6. Loan calculator", "7. Exit"]
    for i in menu:
        print(i)

def generate_unique_IBAN():
    iban = 'TB'
    id = str(random.randint(0,5)).zfill(4)
    iban += id
    if iban not in ibans:
        print(iban)
        ibans.append(iban)
        return
    else:
        generate_unique_IBAN()
        






