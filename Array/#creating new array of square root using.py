#creating new array of square root using while loop 

from array import*

vals=array('i',[10,20,30,40,50])

newArr=array(vals.typecode,(a*a for a in vals))

i=0

while i <len(newArr):
    print(newArr[i])
    i=i+1