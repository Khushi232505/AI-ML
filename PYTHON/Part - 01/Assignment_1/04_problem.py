'''The user enters a string containing a number 
(e.g.,"45").Convert it to : 
• an integer
• a float
• a string again 
Print all three values with their types'''

s = input("Enter a string containing a number: ")

int_value = int(s)
float_value = float(s)
string_value = str(s)

print(int_value, type(int_value))
print(float_value, type(float_value))
print(string_value, type(string_value))
