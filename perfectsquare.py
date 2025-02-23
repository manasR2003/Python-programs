#using function
def perfectSquare(num):
    val=0
    while val*val<=num:
        if val*val==num:
            return 'perfect square'
        else:
            val+=1
    else:
        return 'not a perfect square'
num1=int(input('enter number'))
print(perfectSquare(num1))

#using recursion
def PerfectSquare(num,val=0):
    if val*val>num:
        return 'not a perfect square'
    else:
        if val*val==num:
            return 'perfect square'
        else:
            return PerfectSquare(num,val+1)
num2=int(input('enter number'))
print(PerfectSquare(num2))