#New array creating

from array import*

vals=array('i',[10,20,30,40,50])

newArr=array(vals.typecode,(a for a in vals))
               
print(newArr)