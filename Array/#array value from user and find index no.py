#array value from user and find index no also 

from array import*
arr=array('i',[])
n=int(input("Enter the length of the array"))

for i in range(n):
    x=int(input("Enter the next values")) #store in x element
    arr.append(x)
print(arr)

val=int(input("Enter the values that you want to search"))
k=0 #index no
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1

