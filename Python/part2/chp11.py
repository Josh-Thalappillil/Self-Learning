import random
# Build a text based magic 8 ball program where the user can shake a magic eight ball and get predictions about their future

# ask user to shake the ball
# print randomise variety of strings

def eightball():
    ques = input("Ask any question now and shake the ball by typing 8. ")
    ans = random.randint(1, 4)
    
    if ques == "8":
        if ans == 1:
            print("You most definitely will.")
        elif ans == 2:
            print("It is uncertain at this point in time.")
        elif ans == 3:
            print("You most definitely will not.")
        elif ans == 4:
            print("mimi")

    else:
        print("Please try again.")

    

eightball()

