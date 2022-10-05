#printing with a return
def maths(x):
    return x * 2
    

result = maths(2)
print(result)


#printing even or odd numbers using a function
def even_odd(x):
    if x % 2 == 0: print("even")
    else:
        print("odd")
even_odd(22) 
even_odd(35)

#parameters
def f():
    return 1 + 1

result = f()
print(result)

#multiple parameters
def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)

#parameters that can pass

def f(x=10):
    if x == 10:
        print("x is ten")
    else:
        print("x is not 10")

default = f()
pass_in = f(2)



#Nested functions

def nest():
    print("Inner Function!")
    def x():
        print("Nested Function")
    x()


#variables-learning how to interact with global varibales
x = 100
def variable():
    global x
    x += 2
    print(x)


#built in functions

#length
def len():
    print(len("Flabberghasted"))

#data types
def datatypes():
    print(type("Hello World"))
    print(type(100))
    print(type(1.0))

    print(str(100))
    print(int("125"))
    print(float(100))

#inputs
def agetest():

    age = input("How old are you? ")
    age = int(age)
    if age <= 12:
        print("You are a child.")
    elif age >= 13 and age <= 19:
        print("You are a teenager.")
    elif age >=20:
        print("You are an adult.")

