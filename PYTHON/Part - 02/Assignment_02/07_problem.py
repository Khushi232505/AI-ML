''' Design a program to continuously input a number n from user & print if it positive or negative until the user enters “Quit” '''
 
 
while True:
    n = input("enter the number or enter quit to exit : ")
    
    
    if n == "quit" :
        print("Program stopped.")
    break

n = int(n)

if n > 0:
    print("positive number")
elif n < 0:
    print("negative number")
else :
    print("zero")   
