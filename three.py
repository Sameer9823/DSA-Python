a = int(input("Enter the first number: "))  # Input a number
rev = 0
original = a
sum_digits = 0  # Variable name changed for clarity

# Calculate sum of digits
while a:
    sum_digits += a % 10
    a = a // 10

temp = sum_digits  # Store sum of digits for reversing

# Reverse the sum of digits
while temp:
    remainder = temp % 10
    rev = rev * 10 + remainder
    temp = temp // 10

# Check if sum of digits is a palindrome
if sum_digits == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
