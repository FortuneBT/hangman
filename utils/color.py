from typing import List
from random import randint

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



    def multiColored(self,string) -> str:
        """
        this method transform a string in a multi colored string
        """
        self.multiColor.append(self.OKGREEN)
        self.multiColor.append(self.OKBLUE)
        self.multiColor.append(self.OKCYAN)
        self.multiColor.append(self.WARNING)
        self.multiColor.append(self.FAIL)
        self.multiColor.append(self.WHITE)


        solution:str = ""

        #loop to every character in the string to be able to change the color for each of them
        for letter in string:

            nbOfColor = len(self.multiColor)-1

            selectedColor:str = self.multiColor[randint(0,nbOfColor)]

            solution += selectedColor+letter

        return solution+self.ENDC