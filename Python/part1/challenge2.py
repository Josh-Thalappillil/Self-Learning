#Write a function that does something interesting, and use it several times in a program.

print("Hello, this program will calculate and confirm the user's birth year.")

def first():
    name = input("What is your name? ")
    age = input("What is your age? ")
    age = int(age)
    year = int(2022)
    getage = year - age

    print(f"Hello, your name is {name}." )

    if age <= 12:
        print(f"You are a child and you were born in the year {getage}.")
    elif age >= 13 and age <= 19:
        print(f"You are a teenager and you were born in the year {getage}.")
    elif age >=20:
        print(f"You are an adult and you were born in the year {getage}.")
        
def confirm():
    tf = input("Is the previous statement correct? 'True' or 'False'?")
    if tf == "False":
        print("Please restart the program and try again.")
        return False
    else:
        print("Thank you for using this program.")
        return True


first()
confirm()
