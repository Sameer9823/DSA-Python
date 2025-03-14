a = int(input("Enter the first number: "))
rev = 0
original = a
while a:
    remainder = a % 10
    rev = rev * 10 + remainder
    a = a // 10
    
if original == rev:
    print('it is the palindrome')
else:
    print('it is not the palindrome')

