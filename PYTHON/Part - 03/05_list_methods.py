''' l.append(val) --> add one element at the end
l.insert(idx,val) --> insert elemnt at IndexError
l.sort() --> arranges in increasing order
l.reverse() --> reverses the order
l.pop(idx) --> remove the element from that particular index  
l.remove(val) --> remove the given element  '''

num = [8, 5, 67, 45, 3, 9]

num.append(10)
print(num)

# num.extend("abc") # it is used to just divide the string into sigle single characters


num.insert(2, 4)
print(num)

num.sort()
print(num)

num.reverse()
print(num)

num.pop(4)
print(num)

num.remove(10)
print(num)

print(max(num))
