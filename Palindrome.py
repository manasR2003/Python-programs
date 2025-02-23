#using function
def palindrome(num,rev=0):
    temp=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev==temp
num1=int(input('enter number'))
print('palindrome' if palindrome(num1)==True else 'not a palindrome')

#using recursion
def Palindrome(num,rev=0):
    if num==0:
        return rev
    else:
        return Palindrome(num//10,rev*10+num%10)
num2=int(input('enter number'))
print('palindrome' if Palindrome(num2)==num2 else 'not a palindrome')