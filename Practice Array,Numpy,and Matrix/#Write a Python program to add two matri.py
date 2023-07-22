#Write a Python program to add two matrices using NumPy.


from numpy import*

arr1=array([ 
                [1, 2, 3],
                [4, 5, 6],
                [3, 4, 5]



                ])
arr2=array([
                [3, 4, 5],
                [3, 4, 5],
                [2, 3, 4]



            ])

arr3=arr1+arr2
print(arr3)