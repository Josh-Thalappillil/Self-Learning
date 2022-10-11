# Continuing from chapter 5 learning about lists and tuples

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

dictionary()

