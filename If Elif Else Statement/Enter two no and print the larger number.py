#Write a program that asks the user to enter two numbers and prints the larger number.

num1=int(input("Enter 1st no"))
num2=int(input("Enter 2nd no"))

if num1>num2:
    print("The larger no is Num1")
elif num1<num2:
    print("The larger no is Num2")
else:
    print("Both no are equal")