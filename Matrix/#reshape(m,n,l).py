#reshape(m,n,l)

from numpy import*

arr1=array([
                [1,2,3,4,5,6],
                [7,8,9,10,11,12]

             ])


arr2=arr1.reshape(2,2,3)
print(arr2)
