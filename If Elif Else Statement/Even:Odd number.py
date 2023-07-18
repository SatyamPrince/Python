#Question 1: Odd/Even Number
#Write a program that asks the user to enter an integer and determines whether it is an odd or even number. Print the result.

x=int(input("Enter a number"))
r=x%2

if r==0:
    print("Even")

else:
    print("Odd")

