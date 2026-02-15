''' Write a program to check whether two lists share no common elements. 
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4 '''

list1 = [1, 2, 3, 4, 8, 3, 6, 10]
list2 = [ 9, 7, 56, 45]

common_found = False

for item in list1:
    if item in list2:
        common_found= True
        break

if common_found:
    print("the list have common elements")
else:
    print("the list have no common elements")
