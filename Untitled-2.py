# the program for an simple if- statement
score = int(input("Enter the number:"))
if (score >= 45):
    print("student passed exam")
    
# the program for an simple if-else statement
num = int(input("enter the number:"))
if (num % 2 == 0):
    print("number is even")
else:
    print("number is odd")
    
    
# the program for an simple if-elif-else statement
num = int(input("enter the number:")) # the "int" is use for the integer value 
if (num <= 0):
    print("number is negitive")
elif(num % 2 == 0):
    print("positive even number")
else:
    print("positive odd number")
    
# the program is to check the simple Nested-if-statement
n = int(input("Enter the number:"))
if (n >= 45):
    if(n < 30):
        print("the number is less than 30")
    else:
        print("the number is greater than 45")
 
    