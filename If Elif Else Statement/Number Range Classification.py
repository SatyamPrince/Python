#Number Range Classification
#Write a program that asks the user to enter a number and classifies it into different ranges based on the following conditions:

#If the number is between 0 and 10 (inclusive), print "Between 0 and 10."
#f the number is between 11 and 20 (inclusive), print "Between 11 and 20."
#If the number is between 21 and 30 (inclusive), print "Between 21 and 30."
#If the number is greater than 30, print "Greater than 30."
#If the number is less than 0, print "Less than 0."


num=int(input("Enter a number"))

if 0<= num <=10:
    print("Between 0 and 10")

elif 11<= num <=20:
    print("Between 11 and 20")

elif 21<= num <=30:
    print("Between 21 and 30")

elif num>30:
    print("greater than 30")

else:
    print("Less than 0")


