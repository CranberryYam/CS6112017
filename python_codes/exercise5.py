numberFound = 0
x = 11
while numberFound<=20:
    if x%5==0 and x%7==0 and x%11==0:
        print(x)
        numberFound = numberFound + 1
    x = x + 1



