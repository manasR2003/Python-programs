#using function
def disarum(num,pow,res=0):
    while num>0:
        rem=num%10
        res=res+rem**pow
        pow-=1
        num//=10
    return res
num1=int(input('enter number'))
print('disarum' if disarum(num1,len(str(num1)))==num1 else 'not an disarum')

#using recursion
def Disarum(num,pow,res=0):
    if num==0:
        return res
    else:
        return Disarum(num//10,pow-1,res+(num%10)**pow)
num2=int(input('enter number'))
print('disarum' if Disarum(num1,len(str(num2)))==num2 else 'not an disarum')