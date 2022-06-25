import random

class Player:
    """The person guessing the word.
    
    The responsibility of Player is to keep track of the letters guessed and the change in parachute.
    
    Attributes:
        letters (string): the list of letters in the guess word.
        parachute (string): the change in chute length.
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self._letter = ""

    def get_letters(self):
        """Gets the current letters of the word.
        
        Returns:
            string: the known letters.
        """
        return self._letter

    def add_letters(self, letter):
        """Adds a letter to the guess word.
        
        Args:
            self (Player): an instance of Player.
            letter (string): the given letter.
        """
        self._letter = letter