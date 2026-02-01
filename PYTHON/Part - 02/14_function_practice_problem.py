# Calculate average of three numbers.

'''def avg(a,b,c):
    avg = (a+b+c)/3
    return avg

ans = avg(2,4,6)
print(ans)'''


# default value
# default arguement always come at the last 

'''def sum(a, b=1):
    return a+b

print(sum(5))'''



#Check whether the number is even or odd
def check_even_odd(a):
    if (a%2==0):
        return "even"
    else :
        return "odd"
    
result = check_even_odd(8)
print(result)
