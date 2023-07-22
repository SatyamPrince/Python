#variable length

def sum(a,*b):
    print(a)
    print(b)
    
    
    c=a
    for i in b:
       c=c+i
    print(c)

sum(5,6,34,78)