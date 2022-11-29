#A basic calculator that provides the sum of two inputs
#Additional learning from 'Programming with Mosh' on YouTube

def calc():

    first = float(input("First: "))
    second = float(input("Second: "))
    sum = first + second
    print(f"Sum: {sum}")
    return sum

def minus(num):
    return num - 5



def temp():
    temperature = float(input("What is the temperature today? "))

    if temperature >= 30:
        print("The weather today is hot.")
    elif temperature >= 20:
        print("The weather is warm today.")
    elif temperature > 10:
        print("The weather is a bit cold today")
    else:
        print("It is very cold today.")


def weight():
    weight = float(input("What is your weight? "))
    unit = input("(K)g or (L)bs: ")

    if unit.upper() == "K":
        converted = round(weight / 0.45)
        print("Weight in lbs: " + str(converted))
    else:
        converted = round(weight * 0.45)
        print("Weight in Kg:" + str(converted))

#loops
def loop():

    i = 1
    while i <= 10:
        print(i * '*')
        i += 1

#lists
def name():
    names = ["John", "Bob", "Josh", "Jeannie", "Mosh"]
    names[0] = "Jon"
    print(names[0:3])
    print(names)
    


def test():
    #loops
    numbers = [1, 2, 3, 4 , 5]
    for item in numbers:
            print(item)
    #range function
    for numbers in range(5, 10 , 2):
            print(numbers)





