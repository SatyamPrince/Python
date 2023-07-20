#three int l,r,k fine how many no aur divisble by k not number only count and input should be in one line

l,r,k=input("Enter the values of l,r and k").split()

l=int(l)
r=int(r)
k=int(k)

count=0

for i in range(l,r+1):
    if(i%k==0):
        count=count+1
        
else:
    print(count)
