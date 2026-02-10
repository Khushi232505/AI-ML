''' Dictionary --> key:value pairs. Its is mutable, unordered, indexed.
It cannot contain duplicate keys. '''

dict = {
    "name" : "khushi",
    "cgpa" : 9.2,
    "subjects" : ["maths", "science"],
    3.14 : "PI",   
}

dict["cgpa"] = 9.8

print(dict)
print(len(dict))
print(type(dict))
print(dict["name"])

dict = {} # empty dictionary
