#using function
def perfectNum(num,sum=0):
    for i in range(1,num//2+1):
        if num%i==0:
            sum=sum+i
    if sum==num:
        return 'perfect Number'
    else:
        return 'not a perfectNumber'
num1=int(input('enter number'))
print(perfectNum(num1))

#using recursion
def PerfectNumber(num,val=1,sum=0):
    if val>num//2+1:
        return sum==num
    else:
        if num%val==0:
            return PerfectNumber(num,val+1,sum+val)
        else:
            return PerfectNumber(num,val+1,sum)
num2=int(input('enter a number'))
print('perfect number' if PerfectNumber(num2)==True else 'not a perfect number')