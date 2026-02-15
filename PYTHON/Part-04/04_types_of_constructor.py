class Student:
    def __init__(self):
        print("object is being constructed")
        
    # def __init__(self,name, cgpa): #Parameterized Constructors
    #     self.name = name  
    #     self.cgpa = cgpa
        
    # def get_cgpa(self): # stu1
    #     return self.cgpa #instance methods
    
    
# stu1 = Student("khushi", 8.9)
# stu2 = Student("yuvraj", 7.6)
# stu3 = Student("anupam", 8.5)

# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")


'''  default parameter --> it only have one parameter(self)

Parameterized Constructors - Takes parameters to initialize values uniquely for each object.

Note - Python doesn’t support constructor overloading directly (like Java/C++) i.e. having multiple constructors in the same class. Whichever is written last is executed.  '''

