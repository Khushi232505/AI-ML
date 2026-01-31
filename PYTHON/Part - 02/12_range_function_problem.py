# Print sum of first 'n' atural numbers.

n = int(input("enter the number: "))

sum = 0

for i in range(1,n+1):
    sum += i

print("the sum is: ", sum)
