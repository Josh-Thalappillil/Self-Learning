#Write a program with a variable called age assigned to an integer that prints different strings depending on what integer age is.
#Variable is age
#variable is assigned to an integer
#prints strings depending on integer age

def age():
    age = int(input("Please enter your age: "))
    
    if age <= 12:
        print("You are a child.")
    
    elif age >= 13 and age <= 19:
        print("You are a teenager.")
    
    elif age >= 20:
        print("You are an adult.")


age()
