#convert 2d array to 1d array and thn 1d array to 3d array


from numpy import*

arr1=array([
                [1,2,3,4,5,6],
                [7,8,9,5,3,4]


            ])



arr2=arr1.flatten()
arr3=arr2.reshape(3,4)


print(arr3)

