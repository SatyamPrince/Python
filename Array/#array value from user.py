#array value from user 

from array import*

arr=array('i',[])

n=int(input("Enter the length of number"))

for i in range(n):
    x=int(input("Enther the next value"))
    arr.append(x)

print(arr)