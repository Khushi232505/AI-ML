''' Given a tuple of integers, create:
1 -- A tuple of all even numbers
2 -- A tuple of all odd numbers '''

tup = (9, 6, 4, 8, 56, 34, 89, 67, 3, 2, 45, 10)
print(len(tup))

even = ()
odd = ()

for i in tup:
    if (i % 2 == 0):
        even = even + (i,)
    else :
        odd = odd + (i,)
   
print("Even numbers tuple:", even)
print("Odd numbers tuple:", odd)
