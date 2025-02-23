#using function
def lcm(n1,n2,l=0):
    if n1>n2:
        l=n1
    else:
        l=n2
    while True:
        if l%n1==0 and l%n2==0:
            return  l
        else:
            l+=1
num1=int(input('enter a number'))
num2=int(input('enter a number'))
print(lcm(num1,num2))

#using recursion
def check(n1,n2):
    if n1>n2:
        return lcm(n1,n1,n2)
    return lcm(n2,n1,n2)
def lcm(l,n1,n2):
    if l%n1==0 and l%n2==0:
        return l
    return lcm(l+1,n1,n2)
num3=int(input('enter a number'))
num4=int(input('enter a number'))
print(check(num3,num4))
        