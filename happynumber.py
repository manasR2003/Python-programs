#uding function
def happy(num):
    while num>9:
        sq=0
        while num>0:
            rem=num%10
            sq=sq+rem**2
            num//=10
        num=sq
    else:
        if num==1 or num==7:
            return 'Happy number'
        return 'Not a happy number'
num1=int(input('enter a number'))
print(happy(num1))


#using recursion
def sq(num,sum=0):
    if num==0:
        return sum
    return sq(num//10,sum+(num%10)**2)
def Happy(num):
    if num<10:
        return num==1 or num==7
    return Happy(sq(num))
num2=int(input('enter a number'))
print('Happy number' if Happy(num2)==True else 'Not a happy number')
