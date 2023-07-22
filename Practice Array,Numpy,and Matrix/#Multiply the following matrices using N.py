#Multiply the following matrices using NumPy: A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]].

from numpy import*

m1=matrix('1 2;3 4')
m2=matrix('5 6;7 8')

m3=m1*m2

print(m3)

