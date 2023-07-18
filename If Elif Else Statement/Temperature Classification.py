#Temperature Classification
#Write a program that asks the user to enter the temperature in Celsius and classifies it into different categories based on 
#the following conditions:

#Below 0: "Freezing"
#0 to 10: "Cold"
#11 to 20: "Moderate"
#21 to 30: "Warm"
#Above 30: "Hot"

temp=float(input("Enter the temp"))

if temp<0:
    print("Freezinf")
elif temp<=10:
    print("Cold")
elif temp<=20:
    print("Moderate")
elif temp<=30:
    print("Warm")
else:
    print("Hot")




