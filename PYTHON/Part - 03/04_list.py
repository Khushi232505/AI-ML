# list are mutable

marks = [99, 89, 100, 65, 92, "abc"]

marks[2] = 70

print(type(marks))
print(len(marks)) # lemght of string
print(marks[2])

# list slicing

print(marks[0:5])
# the default value of starting string is 0 and the default value for the ending index is the lenght of the list
