from typing import List
from random import Random, randint
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

        #to create the variable word_to_find
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
        firstTime:bool = True
        
        while self.lives > 0:
            os.system("clear")
            if firstTime == True:
                #to get the first choice of the user and to have a différent message at the beginning
                print("-"*10 + "-"*len(" LET'S PLAY HANGMAN ") + "-"*10)
                print("-"*10 + " LET'S PLAY HANGMAN " + "-"*10)
                print("-"*10 + "-"*len(" LET'S PLAY HANGMAN ") + "-"*10)
                print()
                print(self.correctly_guessed_letters)
                self.playerEntry = input("\nChoose your first letter : ")

            #this loop will continue until there is only one characte 
            while len(self.playerEntry) != 1:
                os.system("clear")
                self.showStats()
                self.playerEntry = input("No no no !!! You're only allow to put ONE character: ")
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
                else:
                    #executed if the the letter is NOT FOUND
                    os.system("clear")
                    self.lives -= 1
                    self.wrongly_guessed_letters.append(self.playerEntry)
                    self.error_count += 1
                    self.showStats()
                    result = False

                #check if it is a victory
                if self.word_to_find == self.correctly_guessed_letters:
                    self.well_played()
                    break

                #check if i have already use all my lives at the last chance
                if self.lives != 0:
                    if result == False:
                        self.playerEntry = input(f"{self.bcolors.FAIL}That's the WRONG answer!!! Try again : {self.bcolors.WHITE}")
                    else:
                        self.playerEntry = input(f"{self.bcolors.OKGREEN}That's a GOOD answer!!! Please continue: {self.bcolors.WHITE}")
                
        
            firstTime = False
        else:
            self.showStats()
            self.game_over()
    

    def showStats(self):
        print(f"self.lives : {self.lives}")
        print(f"self.wrongly_guessed_letters : {self.wrongly_guessed_letters}")
        print(f"self.correctly_guessed_letters : {self.correctly_guessed_letters}") 
        print(f"playerEntry : {self.playerEntry}")
        print(f"self.turn_count : {self.turn_count}")

    def start_game(self):
        """
        method that will start the game and will call the method
        play() ntil the game is over (because the use guessed the word or because of a game over).
        will call game_over() if lives is equal to 0.
        will call well_played() if all the letter are guessed.
        will print well_guessed_letters, bad_guessed_letters, life, error_count and turn_count at 
        the end of each turn.
        """
        self.play()

    def game_over(self):
        """
        method that will stop the game and print the end message
        """
        os.system("clear")
        #this method should STOP the game too
        print("game over...")

    def well_played(self):
        """
        Method that will print the positive message when we win
        """
        os.system('clear')
        word = "".join(self.word_to_find)
        print(f"{self.bcolors.OKGREEN}You found the word {self.bcolors.WARNING}\"{word}\" {self.bcolors.OKGREEN}in {self.bcolors.BOLD} {self.turn_count} {self.bcolors.ENDC} {self.bcolors.OKGREEN}turns with {self.bcolors.FAIL}{self.error_count} {self.bcolors.OKGREEN}errors!")

class Bcolors():
    """
    a class using the color code for a code easier to read
    """
    def __init__(self) -> None:
        
        self.NORMAL:str = "\033[0"
        self.BRIGHT:str = "\033[1"
        self.BOLD:str = '\033[1m'
        self.UNDERLINE:str = '\033[4m'

        self.OKBLUE:str = '\033[94m'
        self.OKCYAN:str = '\033[96m'
        self.OKGREEN:str = '\033[92m'
        self.WARNING:str = '\033[93m'
        self.FAIL:str = '\033[91m'
        self.WHITE = '\033[0m'
        
        self.HEADER:str = '\033[95m'
        self.ENDC:str = '\033[0m'
        

        self.multiColor:List[str] = []

    def disable(self) -> None:
        """
        method desactivating the color in all the string
        """
        self.NORMAL = ""
        self.BRIGHT:str = ""

        self.OKBLUE:str = ""
        self.OKCYAN:str = ""
        self.OKGREEN:str =""
        self.WARNING:str =""
        self.FAIL:str = ""
        self.WHITE = ""

        self.ENDC:str = ""
        self.BOLD:str = ""
        self.HEADER:str = ""
        self.UNDERLINE:str = ""

    def multiColored(self) -> str:
        self.multiColor.append(self.OKGREEN)
        self.multiColor.append(self.OKBLUE)
        self.multiColor.append(self.OKCYAN)
        self.multiColor.append(self.WARNING)
        self.multiColor.append(self.FAIL)
        self.multiColor.append(self.WHITE)
        return self.multiColor(randint(0,len(self.multiColor)))


