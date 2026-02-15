class Student:
    def __init__(self,name, cgpa):
        self.name = name #instance attributes
        self.cgpa = cgpa   #instance attributes 
    
stu1 = Student("khushi", 8.9)
stu2 = Student("yuvraj", 7.6)
stu3 = Student("anupam", 8.5)


print(stu1.name, stu1.cgpa)
print(stu2.name)
print(stu3.name)
