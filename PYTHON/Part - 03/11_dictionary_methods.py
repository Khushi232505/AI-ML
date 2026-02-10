dict = {
    "name" : "khushi",
    "cgpa" : 9.2,
    "subjects" : ["maths", "science"],
    3.14 : "PI",   
}

dict_keys = list(dict.keys())
print(type(dict_keys))

# print(dict.keys()) # returns all keys

# print(dict.values()) # returns all values

# print(dict.items()) # returns (key, val) pairs

# print(dict.get("cgpa")) # returns value according to the key
# print(dict.get("cgpa2")) # wrong key --> returns none
# # print(dict["cgpa2"])  # it returns error
 
# dict.update({"khushi":"love"}) # add a new item to dictionary
# print(dict)


# # print(dict.clear()) # removes all the item from the dictionary

# dict.pop("name") # remove the particular item from the dictionary and if the key not found, returns default.
# print(dict)

# print(dict.popitem()) # removes every item from the dictionary and only returns the last inserted key:value pair as a tupple
