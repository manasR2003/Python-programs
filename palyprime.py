#using function
def prime(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        else:
            return True
    else:
        return False
def palindrome(num,rev=0):
    temp=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev==temp and prime(rev)
num1=int(input('enter nnumber'))
print('palyprime number' if palindrome(num1)==True else 'not a palyprime number')

#using recursion
def Prime(num,val=2):
    if val<int(num**0.5)+1:
        return True
    else:
        if num%val==0:
            return False
        else:
            return Prime(num,val+1)
def Palyprime(num,dup,rev=0):
    if num==0:
        return rev == dup and prime(rev)
    else:
        return Palyprime(num//10,dup,rev*10+num%10)
num2=int(input('enter number'))
print('palyprime number' if Palyprime(num2,num2)==True else 'not a palyprime number')