import random
ibans = []
def generate_unique_iban():
    while True:
        iban = "TB"
        id = str(random.randint(1,9999)).zfill(4)
        iban +=id
        if iban not in ibans:
            ibans.append(iban)
            return iban
        
print(generate_unique_iban())
