username = input("enter the username: ")
password = input("enter the password: ")

if (username == "admin" and password == "pass") :
    print("you have sucessfully loggedin")
else:
    if (username != "admin"):
        print("wrong username")
    else :
        print("wrong password")
        
        
'''Nesting means putiing some another conditon under the previous condition'''

'''elif AND else can not be used individually without the if condition but the if condition can be used independently'''
