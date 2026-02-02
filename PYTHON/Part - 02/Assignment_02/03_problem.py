''' Write a function that prints the digits of a number, n .
For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them. '''

n = int(input("enter the num :"))
def num(n):
    n = abs(n) # to avoid negative nnumbers
    digits = []
    
    while n > 0:
        digit = n % 10  # figure out the last digit
        digits.append(digit)   
        n = n // 10   # removes the last digit
        
    for d in reversed(digits):
        print(d)
        
num(n)

'''  % 10 → digit nikaalta hai

append() → digit ko save karta hai

reversed() → order theek karta hai '''
