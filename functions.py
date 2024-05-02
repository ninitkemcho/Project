import random
from account_creation import add_account, accounts
import functions


   
def main():
    while True:
        functions.menu()
        choice = int(input("Enter number: "))
        if choice == 1:
            name = input("To create account, enter your name: ")
            while True:
                amount = int(input("Enter initial balance (0 -> 100): "))
                if amount > 100:
                    print("Initial balance should not be more than 100 GEL")
                else:
                    break           
            unique_IBAN = functions.generate_unique_IBAN()
            add_account(name, amount, unique_IBAN)
            print(f"Account added successfully with IBAN: {unique_IBAN}")
        elif choice == 7:
            break

if __name__ == "__main__":
    main()

