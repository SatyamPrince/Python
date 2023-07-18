#creating new arr square root using for loop

from array import*

vals=array('i',[10,20,30,40,50])

newArr=array(vals.typecode, (a*a for a in vals))

for i in newArr:
    print(i)