def decimal2binary(number) -> list:
    out = []
    if  number>0:
        out.append(number%2)
        decimal2binary(int(number/2))
    else:
        out.append(0)
        return out

def decimalToBinary(n):
    assert int(n)== n, 'The parameter must be an integer only!!'
    if n/2 == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(13))


print(decimal2binary(13))