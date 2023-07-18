#array value from user and find index value using function
from array import*
arr=array('i',[])
n=int(input("Enter the length of the array")) 
for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)
print(arr)

vals=int(input("Enter the values that you want to search"))

print(arr.index(vals))

