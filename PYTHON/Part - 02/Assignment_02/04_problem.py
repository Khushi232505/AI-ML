''' Q4. Write a function to return the count the number of digits in a number, n . '''
 
 

def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    
    count = 0
    while n>0:
        count += 1
        n = n//10
    return count
    
print(count_digits(865432357900766433))
        
      
        
    
