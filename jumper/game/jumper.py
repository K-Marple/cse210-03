import random

class Jumper:
    """The person jumping with parachute.
    
    The responsibility of Jumper is to keep track of the guess word and the parachute length.
    
    Attributes:
        _word (string): the word being guessed.
        _parachute (string): visual representation of number of guesses left.
    """

    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._word = ""
        self._letters = ""

    def get_lives_left(self):
        """Gets a response for the player. Whether letter was correct or not.
        
        Args:
            self (Jumper): an instance of Jumper.
            
        Returns:
            string: a reponse for the player.
        """
        lives = 5
        if self._letters in self._word:
            lives = lives
        elif self._letters not in self._word:
            lives -= 1
        
        if lives == 5:
            return """
        /`~~~~~~~~`\ 
        \_,_,_,_,_,/ 
         \        / 
          \      / 
           |    | 
        \ ( ^.^ ) / 
            )  ) 
            /  \ """
        elif lives == 4:
            return """
        \_,_,_,_,_,/
         \        /
          \      /
           |    |
        \ (‘’*.*`) /
            )  )
            /  \ """
        elif lives == 3:
            return """  
         \        /
          \      /
           |    |
        \ (‘*.*``) /
            )  )
            /  \ """
        elif lives == 2:
            return """
          \      /
           |    |
        \ (``>.< ) /
           )  )
           /  \ """
        elif lives == 1:
            return """
           |    |
        \ (`O_O ) /
            )  )
            /  \ """
        elif lives == 0:
            return """
        ( x_x )
        / )  ) \ 
          /  \ """

    def is_guessed(self):
        """Whether or not the word is correctly guessed.
        
        Args:
            self (Jumper): an instance of Jumper.
            
        Returns:
            boolean: True if the word is guessed; False if not.
        """
        return (self._word == self._letters)

    def watch_secret_word(self, letter):
        """Watches the hidden word be keeping track of letters and blanks in it.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        for self._letter in list(self._word):
            if self._letter in letter:
                print(self._letter, end="")
            else:
                print(" _ ", end="")