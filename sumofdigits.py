def sumofdigit(number) -> int:
    assert number >= 0 and int(number)==number, 'The umber has to be a positive interger only.'
    if number == 0:
        return 0
    else:
        return number%10 + sumofdigit(int(number/10))
        
print(sumofdigit(12))
print(sumofdigit(9867798015))