# Continuing from chapter 5 learning about lists and tuples

from argparse import ONE_OR_MORE
from xmlrpc.client import boolean


def learnlist():
    my_list = ["Apple", "Orange", "Pear", "Dragonfruit", "Avocado", "Tomato"]
    print(my_list[0:5])

def learntup():
    my_tuple = ("brown", "yellow", "white")
    print("brown" in my_tuple)
    
def dictionary():
    my_dictionary = dict()

    my_dictionary["Programming"] = "fun"
    my_dictionary["Programming"]
    print(my_dictionary["Programming"])

    my_dictionary["Bill Gates"] = "rich"
    print(my_dictionary["Bill Gates"])



#Chapter 6 String Manipulation
def upper():
    print("""line one
        line two
        line three
    """ .capitalize())


def chapter6():

    my_dict = {"Sports car":"Skyline", "Modifications":"turbo"}
    for key in my_dict:
        print(key)

    x = 0
    while x < 10:
        print(x)
        x += 1
    print("Happy New Year")

def breaks():
    questions = ["What is your name?", "What is your favorite color?", "What is your quest?"]
    n = 0
    while True:
        print("Type q to quit" + str(n)) 
        answer = input(questions[n]) 
        if answer == "q":
            break 
        n += 1
        if n > 2: 
            n=0



    



