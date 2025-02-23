#using function
def reverse(num,rev=0):
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
num1=int(input('enter number'))
print(reverse(num1))

#using recursion
def Reverse(num,rev=0):
    if num==0:
        return rev
    else:
        return Reverse(num//10,rev*10+num%10)
num2=int(input('enter number'))
print(Reverse(num2))