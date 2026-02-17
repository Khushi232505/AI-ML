class Student:
    def __init__(self, name, grade, percentage, team): 
        self.name = name 
        self.grade = grade 
        self.percentage = percentage 
        self.team = team
        
    def Student_details(self): 
            print(f"{self.name} is in class {self.grade} , with {self.percentage}% from team {self.team}")
  
team1 = "A"
team2 = "B"

   
student1 = Student("khushi", 12, 96,team1)
# print(student1.name, student1.grade)

student2 = Student("yuvraj", 11, 95 ,team2)
# print(student2.name, student2.grade)

student1.Student_details()
student2.Student_details()
