num = [8, 5, 67, 45, 3, 9]

x = 45
idx = 0

for val in num:
    if(val == x):
        print(f"{x} found at idx = {idx}")
        break
    idx += 1
    
    
# this is called linear search...
