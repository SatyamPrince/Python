#array value from use with index

from array import*

arr=array('i',[])

n=int(input("Enter the length of a array"))

for i in range(n):
    x=int(input("Enter the array values"))
    arr.append(i)

print(arr)

val=int(input("Enther the values that want to search"))

k=0

for e in arr:

    if e==val:
        print(k)
        break
    k=k+1

