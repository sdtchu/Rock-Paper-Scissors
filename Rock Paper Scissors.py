import random
import math

def play():
    moves = ['r', 'p', 's']
    user_choice = input("Please enter rock ['r'], paper ['p'], or scissors ['s']?\n")
    com_choice = random.choice(moves)
    print(winner(user_choice, com_choice))

def winner(user, com):
    if user == com:
        return "You both chose {}. It's a tie!".format(user)
    if user == 'r' and com == 's' or user == 's' and com == 'p' or user == 'p' and com == 'r':
        return "You chose {} and the computer chose {}. You win!".format(user, com)
    elif com == 'r' and user == 's' or com == 's' and user == 'r' or com == 'p' and user == 's':
        return "You chose {} and the computer chose {}. You lost.".format(user, com)

def best_of():
    num = int(input("How many games would you like to play?"))
    for i in range(num):
        play()
    

best_of()