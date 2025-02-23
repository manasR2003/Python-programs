#using function
def amstrong(num,pow,res=0):
    while num>0:
        rem=num%10
        res=res+rem**pow
        num//=10
    return res
num1=int(input('enter number'))
print('amstrong' if amstrong(num1,len(str(num1)))==num1 else 'not an amstrong')

#using recursion
def Amstrong(num,pow,res=0):
    if num==0:
        return res
    else:
        return Amstrong(num//10,pow,res+(num%10)**pow)
num2=int(input('enter number'))
print('amstrong' if Amstrong(num1,len(str(num2)))==num2 else 'not an amstrong')