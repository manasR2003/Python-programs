#using function
def fibo(num,a=0,b=1,c=0):
    count=1
    while count<num:
        a=b
        b=c
        c=a+b
        count+=1
    return c
num1=int(input('enter a number'))
print(fibo(num1))

#using recursion
def Fibo(num):
    if num==1 or num==2:
        return num-1
    return Fibo(num-1)+Fibo(num-2)
num2=int(input('enter a number'))
print(fibo(num2))