s ={1, 2, 2, 2, 3}

print(len(s))

s.remove(3) # remove the particular element from the set and return the rest of the set
print(s)

s.add(9) # adds the elements in the set
print(s)

s.discard(9)
print(s)

s.pop() # removes the random value
print(s)

s.clear()
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.union(s2)) # returns new union
print(s1.intersection(s2)) # returns new intersection
