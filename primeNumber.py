# using function
def prime(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return 'not a prime number'
        else:
            return 'prime number'
    else:
        return 'not a prime number'
num1=int(input('enter number'))
print(prime(num1))        

#using recursion
def Prime(num,val=2):
    if val<int(num**0.5)+1:
        return 'prime number'
    else:
        if num%val==0:
            return 'not a prime number'
        else:
            return Prime(num,val+1)
num2=int(input('enter number'))
print(Prime(num2))