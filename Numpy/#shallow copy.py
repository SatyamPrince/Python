#shallow copy

from numpy import*

arr1=array([1,2,3,4,5])

arr2=arr1.view()  # if we update an element in one array then the changes would also be reflected in another array.


arr1[1]=6

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

