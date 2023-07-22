#pass list inside funtion 

#check how many no are even and odd inside a list 

def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd



lst=[23,20,34,5,23,45,40,30,32]
even,odd=count(lst)

print(even)
print(odd)

