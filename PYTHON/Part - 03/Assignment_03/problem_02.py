# Given a list of integers compute the average of all numbers in the list.

l1 = [2, 3, 4, 8, 9, 6]

total = 0
i = 1

for i in l1:
    total = i + total
    i += 1
    
average = total/i
print("average : ", average)
    
