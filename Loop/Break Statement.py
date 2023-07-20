#Break Continue Pass

x=int(input("How many candied do you want?"))

av=5

i=1
while i<=x:
    if i>av:
        print("Out of stock")
        break                      #The break statement is used to terminate a loop prematurely when a certain condition is met. 
    print("Candies")
    i=i+1

print("Bye")