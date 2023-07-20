#print the no which is divible by 5 out of a list.

nums=[15,32,31,61,70]

for num in nums:
    if num%5==0:
        print(num)
        break

else:
    print("Not found")

    
