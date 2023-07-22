#Write a Python program to multiply two matrices using NumPy.

from numpy import*

m1=matrix('1 2 3;4 5 6;7 5 4')
m2=matrix('2 3 2;4 3 4;2 3 5')

m3=m1*m2
print(m3)
