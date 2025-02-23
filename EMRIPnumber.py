#using function
def prime(num):
    for val in range(2,int(num**0.5)+1):
        if num%val==0:
            return False
    else:
        return True
def check(num,rev=0):
    temp=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    if temp!=rev:
        if prime(temp)==prime(rev):
            return 'EMRIP number'
        return "Not an EMRIP number"
num1=int(input('enter nnumber'))
print(check(num1))

#using recursion
def Prime(num,val=2):
    if val<int(num**0.5)+1:
        return True
    else:
        if num%val==0:
            return False
        else:
            return Prime(num,val+1)
def Check(num,dup,rev=0):
    if num==0:
        return rev != dup and prime(rev)==prime(dup) 
    else:
        return Check(num//10,dup,rev*10+num%10)
num2=int(input('enter nnumber'))
print('EMRIP number' if Check(num2,num2)==True else 'not an EMRIP number')