# Given a list, print all elements that appear more than once in the list.

list = ["khushi", 23, 90, 45, "anupam", 23 , "khushi", 1.1, 90, 1.1]


repeated =[]

for item in list:
    if list.count(item) > 1 and item not in repeated:
        repeated.append(item)
    
print("elements appearing more than once:  ", repeated)
