from typing import List

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
        

    def play(self):
        pass

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
