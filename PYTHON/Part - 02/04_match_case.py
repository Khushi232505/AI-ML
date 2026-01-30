# MATCH CASE are the alternate for if-elif-else 

color = input("enter color: ")

match color:
    case "green":
        print("go")
    case"yellow":
        print("look")
    case"red":
        print("stop")
    case _:
        print("wrong color")
        
