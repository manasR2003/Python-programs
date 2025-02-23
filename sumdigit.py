#using function
def sumdigit(num,sum=0):
    while num>0:
        rem=num%10
        sum=sum+rem
        num//=10
    return sum
num1=int(input('enter number'))
print(sumdigit(num1))

#using recursion
def SumDigit(num,sum=0):
    if num==0:
        return sum
    else:
        return SumDigit(num//10,sum+num%10)
num2=int(input('enter number'))
print(SumDigit(num2))