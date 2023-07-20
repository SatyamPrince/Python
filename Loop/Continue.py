#print the no bt 1 to 100 but divisible by 3 or 5

for i in range(1,101):
    
    if i%3==0 or i%5==0:
        continue  #The continue statement is used to skip the current iteration of a loop and move on to the next iteration.

    print(i)


print("Bye")