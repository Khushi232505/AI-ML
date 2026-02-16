class Student:
    college_name = "bbdu" # class attributes
    PI = 3.14
    
    def __init__(self, name, cgpa): #instance attributes
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.1
        
stu1 = Student("khushi", 9.86)

print(Student.college_name)  #class attribute can also be accessed with class name
print(stu1.college_name)
print(stu1.name)
print(stu1.PI)
