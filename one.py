#amstromg
a = int(input("Enter the first number: "))
b = 0
temp = a 

while temp:
    last=temp%10
    temp//=10
    b = b+(last**3)
    
if b==a:
    print('yes')
else:
    print('No')