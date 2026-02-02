'''Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
• If salary < 30,000 → 5%
• If salary is 30,000-70,000 → 15%
• If salary > 70,000 → 25%  '''

salary = int(input("enter the salary: "))

if salary < 30000:
    print("the final tax rate is 5%")
    
elif (salary >= 30000 and salary <= 70000):
    print("the final tax rate is 15%")
    
else :
    print("the final tax rate is 25%")
