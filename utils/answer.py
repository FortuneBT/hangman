from typing import List

class Answer():
    """
    this class is to check the answer even if the answer is a bit incomplet or in french
    """
    def __init__(self,response:str = "No") -> None:
        self.response = response.upper()
        self.answerYes: List[str] = ["Y","YE","YES","O","OU","OUI"]
        self.answerNo: List[str] = ["N","NO","NON"]
        self.give()

    def give(self) -> bool:
        """
        methode who give the choice
        """
        
        #choice will be, True for yes and False for no
        choice:bool = False

        if self.response in self.answerNo:
            choice = False
                
        
        if self.response in self.answerYes:
            choice = True  
        
        return choice
    

    def check(self) -> bool:

        """
        check is to know if the answer is valide or not (bein in list yes or list no)
        """
        
        matching:bool = False

        #if it is true, it means there is an answer found in the no list
        if self.response in self.answerNo:
            matching = True

        #if it is true, it means there is an answer found in the yes list
        if self.response in self.answerYes:
            matching = True

        return matching