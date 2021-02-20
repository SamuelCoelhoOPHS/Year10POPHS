while True: 

    print("Welcome, please enter your following info:") 

    email=input("enter your email address: \n")
    skill_level=input("Choose your Skill Level (C)Casual/(E)Expert: \n")
    country=input("enter country UK/US/AU: \n")


    if skill_level == "C" and "UK" : 
        print("Casual selected, The UK fee is: 30 GBP")
    elif skill_level == "E" and "UK" :
        print("Expert selected, The UK fee is: 45 GBP")
    else : 
        print("Invalid selection")

    if skill_level == "C":

        skill_level = "Casual"

    elif skill_level == "E":

        skill_level = "Expert"

    if skill_level == "C" and "US" : 
        print("Casual selected, The US fee is: 45.0 USD")
    elif skill_level == "E" and "US" :
        print("Expert selected, The US fee is: 67.5 USD")
    else : 
        print("Invalid selection")


        break
