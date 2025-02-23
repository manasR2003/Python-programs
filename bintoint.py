#using function
def bintoint(num,pow=0,sum=0):
    while num>0:
        rem=num%10
        sum=sum+rem*2**pow
        pow+=1
        num//=10
    return sum
num1=int(input('enter number'))
print(bintoint(num1))

#using recursion
def Bintoint(num,pow=0,sum=0):
    if num==0:
        return sum
    return Bintoint(num//10,pow+1,sum+(num%10)*2**pow)
num2=int(input('enter number'))
print(Bintoint(num2))