from typing import List
from random import Random, randint


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

        firstTime = True
        
        while self.lives > 0:
            
            if firstTime == True:
                #to get the choice of the user
                self.playerEntry = input("Let's play! You're allow to enter one character : ")

            #this loop will continue until there is only one characte 
            while len(self.playerEntry) != 1:
                self.playerEntry = input("No no no !!! You're only allow to put ONE character: ")
                print("********" + str(len(self.playerEntry)) + "********")
            else:
                self.turn_count += 1

                if self.playerEntry in self.word_to_find:
                    print("''''''''''''trouvé''''''''''''''")
                    self.showStats()
                    result = True
                else:
                    print("non trouvé")
                    self.lives -= 1
                    self.wrongly_guessed_letters.append(self.playerEntry)
                    self.error_count += 1
                    self.showStats()
                    result = False


                if result == False:
                    self.playerEntry = input("That's the WRONG answer!!! Try again : ")
                else:
                    self.playerEntry = input("That's a GOOD answer!!! Please continue: ")
        
            firstTime = False
        else:
            self.showStats()
            self.game_over()
    

    def showStats(self):
        print(f"self.lives : {self.lives}")
        print(f"self.wrongly_guessed_letters : {self.wrongly_guessed_letters}")
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

    def game_over(self):
        """
        method that will stop the game and print the end message
        """
        #this method should STOP the game too
        print("game over...")

    def well_played(self):
        """
        Method that will print the positive message when we win
        """
        print(f"You found the word : {self.word_to_find}")


pendu = Hangman()
pendu.play()
