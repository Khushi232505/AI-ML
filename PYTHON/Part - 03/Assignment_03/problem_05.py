''' Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key ('A', 'B', 'C', 'D') 
depending on the operation they want to perform on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks '''

students = {}

while True :
    print("\nMenu")
    print("A - add a student")
    print("B - Update marks")
    print("C - Search for a students")
    print("D - Display all students and marks")
    print("E - Exit")
    
    choice = input("enter your choice : ").upper()
    
    if choice == "A":
        name = input("enter student name: ")
        marks = int(input("enter marks : "))
        students.update({name:marks})
        print("student added sucessfully")
        
    elif choice == "B":
        name = input("enter student name to update marks : ")
        if students.get(name) is not None:
            marks = int(input("enter new marks : "))
            students.update({name:marks})
            print("marks updated sucessfully")
        else:
            print("student not found")
    
    elif choice == "C":
        name = input("enter student name to search : ")
        result = students.get(name)
        if result is not None:
            print("Marks: ", result)
        else:
            print("Student not found")
            
    elif choice == "D":
        if students :
            for name, marks, in students.items():
                print(name, ":" , marks)
        else:
            print("No student in dictionary")
            
    elif choice == "E":
        print("exiting program")
        break
    
    else:
        print("invalid choice") 
            
