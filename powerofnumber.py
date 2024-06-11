def powerofnumber(num,pow) -> int:
    assert pow >= 0 and int(pow) == pow, 'The power has to be positive integer' 
    if pow == 0:
        return 1
    if pow == 1:
        return num
    return num * powerofnumber(num,pow-1)
    
print(powerofnumber(2,4))