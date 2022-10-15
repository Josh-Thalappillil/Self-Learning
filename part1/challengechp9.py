#

from tokenize import Name

 

def userinput():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    car = input("Enter your favourite car: ")

    my_file = open("my_file.txt", "w")
    my_file.write(f"Your name is {name}, you are {age} years old and your favourite car is the {car}.") 
    my_file.close()
    readinput()

def readinput():
    
    with open("my_file.txt", "r") as my_file: 
        for line in my_file.read().splitlines():
            print(line) 

userinput()



