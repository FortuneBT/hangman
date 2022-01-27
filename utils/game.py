from time import time
from typing import List
from random import Random, randint
from utils.color import Bcolors
import time
import os


class Hangman():

    def __init__(self) -> None:
        """
        method initialize the attribute of the class 
        """    
        self.possible_words:List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find:List[str] = []
        self.lives:int = 5
        self.correctly_guessed_letters:List[str] = ["_","_","_","_","_"]
        self.wrongly_guessed_letters:List[str] = []
        self.turn_count:int = 0
        self.error_count:int = 0
        self.playerEntry:chr = ""
        self.bcolors = Bcolors()
        

        #select a randomize choice of word in the list (possible_words)
        choice:int = randint(0,len(self.possible_words)-1)

        #to create the variable word_to_find that contain the list of character of the word we want to find
        for letter in self.possible_words[choice]:
            self.word_to_find.append(letter)

        #allow to have the exact number of underscore
        self.correctly_guessed_letters = []
        for letter in self.word_to_find:
            self.correctly_guessed_letters.append("_")
        
        

    def play(self):
        """
        method that asks the player to enter a letter. The player shouldn't be 
        allowed to type something else than a letter, and not more than a letter. If the player
        guessed a letter well, add it to the well_guessed_letters list. If not, i will add it 
        to the wrongly_guessed_letters list and add 1 to error_count.
        """

        os.system("clear")

        #to get the first choice of the user and to have a différent message at the beginning
        if self.firstTime == True:

            self.home()

            print(self.correctly_guessed_letters)

            self.playerEntry = input("\nChoose your first letter : ")

            self.playerEntry = self.playerEntry.lower()

        #this loop will continue until there is only one character 
        while len(self.playerEntry) != 1:

            os.system("clear")

            self.showStats()

            self.playerEntry = input(f"{self.bcolors.FAIL}No no no !!! {self.bcolors.ENDC}You're only allow to put {self.bcolors.FAIL}ONE{self.bcolors.ENDC} character: {self.bcolors.ENDC}")

            self.playerEntry = self.playerEntry.lower()

        else:

            self.turn_count += 1

            #when we are sure there is exactly 1 character then executed the whole code below
            if self.playerEntry in self.word_to_find:

                #executed if the right letter is found

                os.system("clear")

                for x in range(0,len(self.word_to_find)):

                    if self.playerEntry == self.word_to_find[x]:       

                        self.correctly_guessed_letters[x] = self.playerEntry

                self.showStats()
                result = True

                self.playerEntry = input(f"{self.bcolors.OKGREEN}That's a GOOD answer!!! Please continue: {self.bcolors.WHITE}")             

                self.playerEntry = self.playerEntry.lower()

            else:

                #executed if the the letter is NOT FOUND

                os.system("clear")

                self.lives -= 1
                self.wrongly_guessed_letters.append(self.playerEntry)
                self.error_count += 1

                self.showStats()

                result = False

                self.playerEntry = input(f"{self.bcolors.FAIL}That's the WRONG answer!!! Try again : {self.bcolors.WHITE}")

                self.playerEntry = self.playerEntry.lower()
        
    


    def showStats(self):
        """
        This method is necessary to show the state of the game at any moment of the party
        """

        title:str = " LET'S PLAY HANGMAN "

        sizeTitle = len(title)
        
        title = self.bcolors.multiColored(title)

        print("-"*30 + "-"*sizeTitle + "-"*30)
        print("-"*30 + title + "-"*30)
        print("-"*30 + "-"*sizeTitle + "-"*30)

        print()

        print(f"Your lives : {self.lives}")
        print(f"Your wrongly guessed letters : {self.wrongly_guessed_letters}")
        print(f"Your correctly guessed letters : {self.correctly_guessed_letters}") 
        print(f"Your turn count : {self.turn_count}")



    def start_game(self):
        """
        method that will start the game and will call the method
        play() ntil the game is over (because the use guessed the word or because of a game over).
        will call game_over() if lives is equal to 0.
        will call well_played() if all the letter are guessed.
        will print well_guessed_letters, bad_guessed_letters, life, error_count and turn_count at 
        the end of each turn.
        """

        self.firstTime:bool = True
        self.victory:bool = False
        self.gameOver:bool = False

        while self.lives > 0 and self.victory == False and self.gameOver == False:
            
            #check if it is a victory
            if self.word_to_find == self.correctly_guessed_letters:
                print("victory")
                self.victory = True

                self.well_played()

            #check if i have already use all my lives at the last chance
            elif self.lives == 0:    
                print("game over")
                self.gameOver = True
                
                self.game_over()  

            #everything is ok, now we can keep playing
            elif self.word_to_find != self.correctly_guessed_letters or self.lives != 0:
                print("keep playing")
                self.showStats()
            
                self.play()

                self.firstTime = False
        
            



    def game_over(self):
        """
        this method will be the last action executed at the end of the game
        """
        #os.system("clear")

        print(f"{self.bcolors.WARNING}game over...{self.bcolors.ENDC}")

        print()

        input("press Enter to continue ...")

        os.system("clear")

        exit()



    def well_played(self):
        """
        Method that will print the positive message when we win
        """
        #os.system('clear')

        word = "".join(self.word_to_find)

        print(f"{self.bcolors.OKGREEN}You found the word {self.bcolors.WARNING}\"{word}\" {self.bcolors.OKGREEN}in {self.bcolors.BOLD} {self.turn_count} {self.bcolors.ENDC} {self.bcolors.OKGREEN}turns with {self.bcolors.FAIL}{self.error_count} {self.bcolors.OKGREEN}errors!{self.bcolors.ENDC}")

        print()

        input("press Enter to continue ...")

        os.system("clear")


    def home(self):
        """
        method showing the first home page of the game
        """
        title:str = " LET'S PLAY HANGMAN "

        sizeTitle = len(title)

        title = self.bcolors.multiColored(title)

        print("-"*30 + "-"*sizeTitle + "-"*30)
        print("-"*30 + title + "-"*30)
        print("-"*30 + "-"*sizeTitle + "-"*30)
        print()

        print(f"{self.bcolors.WARNING}RULES")
        print("You have to find the word letter by letter or else the hangman is lost")
        print("You have 5 lives in the begining and everytime you miss, you lose 1 live")
        print("Even if you succeed, the count of the turn will be add by 1")
        print(f"You can only choose one character every time{self.bcolors.ENDC}\n")

