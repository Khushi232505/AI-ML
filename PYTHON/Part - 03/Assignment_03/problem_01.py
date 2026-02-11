''' Q1 Ask the user for a string and check whether it is a palindrome or not. A palindrome “madam”, “ is a string which is same when we read it forward & backward. Eg - racecar” etc. '''

str = input("enter the string : ")

new_str = str[::-1]

if(str == new_str):
    print("given string is pallindrome")
else:
    print("given string is not pallindrome")
