#Flatten.convert 2d array to 1d array

from numpy import*

arr1=array([
                [1,2,3],    

                [4,5,6]

            ])

arr2=arr1.flatten()
print(arr2)