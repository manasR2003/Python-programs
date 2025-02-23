def faci(num):
    string=str(num*1)+str(num*2)+str(num*3)
    number='1234567890'
    for ch in string:
        if ch not in number:
            return 'not a facinated number'
    else:
        return 'Facinated number'
num1=int(input('enter number'))
print(faci(num1))

