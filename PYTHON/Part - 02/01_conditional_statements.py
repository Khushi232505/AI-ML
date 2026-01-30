# elif AND else can not be used individually without the if condition but the if condition can be used independently

# 1 -  
'''color = input("enter color: ")

if color == "red":
    print("stop")
elif color == "yellow":
    print("look")
elif color == "green":
    print("go")
else :
    print("wrong color for traffic lights")'''


# 2- 
'''age = int(input("enter age: "))

if (age<13) :
    print("the person is a child")
elif (age >= 13 and age < 18) :
    print("the person is a teenager")
else :
    print("the person is an adult")'''
    
    
# 3 -
'''username = input("enter the username: ")
password = input("enter the password: ")

if (username == "admin" and password == "pass") :
    print("you have sucessfully loggedin")
elif (username != "admin"):
    print("wrong username")
else :
    print("wrong password")'''



# 4 -
n = float(input("enter the number: "))

if (n%5 == 0) :
    print("number is divisble by 5")
else :
    print("number is not divisible by 5")
