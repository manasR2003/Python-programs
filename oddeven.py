#using function
def oddeven(num):
    if num%2==0:
        return 'even'
    return 'odd'
num=int(input('enter number'))
print(oddeven(num))