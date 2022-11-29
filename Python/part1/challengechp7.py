#Write a program that has an infinite loop (with q to quit) 
#and each time through the loop, it asks the user to guess a number 
#and tells them whether their guess was right or wrong.

#boolean, Running = True
#declare guess number (random)
#while loop for running, if user input == guess number, running = false.

import random



def guessgame():
    guess_number = random.randint(1, 10)
    running = True
        
    while running:
        guess = int(input("Enter your guess: "))
        if guess == guess_number:
            running = False
            print("Congratulations, you chose the correct number.")
        
        else:
            print("Guess again.", str(guess_number))
