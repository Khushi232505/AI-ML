''' Write a program that takes a string from the user and prints the number of 
spaces in the string '''

str = input("enter the string : ")

count = 0
for i in str:
    if (i == " "):
        count = count + 1
print("number of spaces : ", count)
