import re

def validate(credit_card):
    if not re.fullmatch(r'[456](\d{3})(-?\d{4}){3}', credit_card):
        return False
    credit_card = credit_card.replace('-', '')
    if re.search(r'(\d)\1{3,}', credit_card):
        return False
    return True
    
for i in range(int(input())):
    if validate(input()):
        print('Valid')
    else:
        print('Invalid')
