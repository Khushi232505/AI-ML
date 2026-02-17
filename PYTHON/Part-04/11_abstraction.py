# Abstraction --> hiding unecessary details from the user through classs and methods

class Student:
    def __init__(self, name, grade, percentage): 
        self.name = name 
        self.grade = grade
        self.percentage = percentage
        
    def Student_details(self): 
            print(f"{self.name} is in class {self.grade}, with {self.percentage+2}% ")

   
student1 = Student("khushi", 12 , 76)
student2 = Student("yuvraj", 11,87)


student1.Student_details()
student2.Student_details()
