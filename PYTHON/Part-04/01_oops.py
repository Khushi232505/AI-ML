#OOPs

# using list --> for creating student records
# student details
''' student_1 = ["khushi", 12]
student_2 = ["yuvraj", 11]

student_1.append("A") 
print(student_1)

print(f"{student_1[0]} is in class {student_1[1]}")
print(f"{student_2[0]} is in class {student_2[1]}") '''

# using OOPs - creating student records

class Student: # student class
    def __init__(self, name, grade, percentage): #__init__ method - constructor , value initialize
        self.name = name #self --> refrence or connection build between class and object
        self.grade = grade # attribute
        self.percentage = percentage # attribute
        
    def Student_details(self): # method
            print(f"{self.name} is in class {self.grade} , with {self.percentage}%")
  
# object - instance of the class      
student1 = Student("khushi", 12, 96)
# print(student1.name, student1.grade)

student2 = Student("yuvraj", 11, 95)
# print(student2.name, student2.grade)

student1.Student_details()
student2.Student_details()

print(student1.__dict__) # in the form of key value pairs

'''OOPs Operations'''

# # modify object properties
print(student1.percentage)
student1.percentage = 99
print(student1.percentage)

# delete object properties
print(student1.__dict__)                    
del student1.percentage
print(student1.__dict__)

# delete object
del student1
print(student1)


