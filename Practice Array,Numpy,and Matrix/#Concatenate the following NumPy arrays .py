#Concatenate the following NumPy arrays horizontally: arr1 = [1, 2, 3] and arr2 = [4, 5, 6].

from numpy import*

arr1=array([1,2,3])
arr2=array([4,5,6])

arr3= (concatenate([arr1,arr2]))

print(arr3)