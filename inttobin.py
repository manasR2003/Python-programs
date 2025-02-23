#using function
def inttobin(num,pow=1,sum=0):
    while num>0:
        rem=num%2
        sum=sum+rem*pow
        pow*=10
        num//=2
    return sum
num1=int(input('enter number'))
print(inttobin(num1))

#using recursion
def Inttobin(num,pow=1,sum=0):
    if num==0:
        return sum
    return Inttobin(num//2,pow*10,sum+(num%2)*pow)
num2=int(input('enter number'))
print(Inttobin(num2))
