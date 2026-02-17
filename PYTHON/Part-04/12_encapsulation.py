class Student:
    def __init__(self, name, grade, percentage, team): 
        self.name = name 
        self.grade = grade 
        self.percentage = percentage 
        
        
    def Student_details(self): 
            print(f"{self.name} is in class {self.grade} , with {self.percentage}% ")
  

student1 = Student("khushi", 12, 96,)
# print(student1.name, student1.grade)

student2 = Student("yuvraj", 11, 95)
# print(student2.name, student2.grade)

student1.Student_details()
student2.Student_details()
