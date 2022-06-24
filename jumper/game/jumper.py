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
        lives = ""
        if self._letter in self._word:
            lives = 5
        elif self._letter not in self._word:
            lives -= 1
        
        if lives == 6:
            print("""
        /`~~~~~~~~`\ 
        \_,_,_,_,_,/ 
         \        / 
          \      / 
           |    | 
        \ ( ^.^ ) / 
            )  ) 
            /  \ """)
        elif lives == 4:
            print("""
        \_,_,_,_,_,/
         \        /
          \      /
           |    |
        \ (‘’*.*`) /
            )  )
            /  \ """)
        elif lives == 3:
            print("""  
         \        /
          \      /
           |    |
        \ (‘*.*``) /
            )  )
            /  \ """)
        elif lives == 2:
            print("""
          \      /
           |    |
        \ (``>.< ) /
           )  )
           /  \ """)
        elif lives == 1:
            print("""
           |    |
        \ (`O_O ) /
            )  )
            /  \ """)
        elif lives == 0:
            print("""
        ( x_x )
        / )  ) \ 
          /  \ """)
        

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
        word_list = ["chemistry", "song", "friendship", "science", "volume", "gate", "literature",
            "philosophy", "construction", "area", "difficulty", "vehicle", "chest", "aspect", 
            "percentage", "agency", "grocery", "girlfriend", "hair", "basket", "length", "equipment", 
            "camera", "wedding", "party"]
        self._word = random.choice(word_list)
        for self._letter in list(self._word):
            if self._letter in letter:
                print(self._letter, end="")
            else:
                print(" _ ", end="")