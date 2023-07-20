#Write a program that prints the sum of all even numbers from 1 to 20 using a while loop.

i=1
sum_even=0

while i<=20:
    if i%2==0:
        sum_even=sum_even+1

    i=i+1

print(sum_even)



