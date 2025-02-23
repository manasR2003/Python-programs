#using function
def factorial(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
num1=int(input('enter number'))
print(factorial(num1))

#using recursion
def Factorial(num):
    if num==0:
        return 1
    return num* Factorial(num-1)
num2=int(input('enter number'))
print(Factorial(num2))