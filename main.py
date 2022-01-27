from utils.game import Hangman
from utils.answer import Answer
import os

#at the begining, since the user decide to run the application, i will choose to automatically do a game
answer = Answer("Yes")

while answer.give() == True:

    appli = Hangman()
    appli.start_game()

    #at the end of the game, propose a new game and check the answer
    result = input("\nDo you want to play again ? ")
    answer = Answer(result)

    #to check if the given answer is valide or not (if it yes or no and no other things)
    while answer.check() == False:
        os.system("clear")
        result = input("Your answer didn't match with our exceptation, please try again.(Yes or No):  ")
        answer = Answer(result)

        