info = [
    ("alice", "math"),
    ("bob", "science"),
    ("alice", "science"),
    ("charlie", "math"),
    ("bob", "math"),
    ("alice", "english"),
    ("charlie", "english"),
]
 
 # 1- part
''' unique_courses = set()

for tup in info :
    unique_courses.add(tup[1]) # course
    
print(unique_courses)'''

# 2 - part
'''for name,course in info:
    if(course == "english"):
        print(name) '''
        
# 3- part
dict = {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else :
        dict[name].add(course)
print(dict)  
