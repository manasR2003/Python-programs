def tech(num):
    dup=num
    if len(str(num))%2==0:
        return (num//(10**(len(str(num))//2))+num%(10**(len(str(num))//2)))**2==dup
    else:
        return False
num=int(input('enter number'))
print('Tech number' if tech(num)==True else 'Not Tech number')
