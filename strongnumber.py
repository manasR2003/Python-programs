#using function
def strong(num):
    sum=0
    while num>0:
        fact=1
        rem=num%10
        for val in range(1,rem+1):
            fact*=val
        sum+=fact
        num//=10
    return sum
num1=int(input('enterr number'))
print('strong number' if strong(num1)==num1 else 'not a strong number')

#using recursion
def Fact(num):
    if num==0:
        return 1
    return num*Fact(num-1)
def Strong(num,sum=0):
    if num==0:
        return sum
    return Strong(num//10,sum+Fact(num%10))
num2=int(input('enterr number'))
print('strong number' if Strong(num2)==num2 else 'not a strong number')

