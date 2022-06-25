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
        word_list = ["chemistry", "song", "friendship", "science", "volume", "gate", "literature",
            "philosophy", "construction", "area", "difficulty", "vehicle", "chest", "aspect", 
            "percentage", "agency", "grocery", "girlfriend", "hair", "basket", "length", "equipment", 
            "camera", "wedding", "party"]
        self._word = random.choice(word_list)
        self._letter = ""
        self._guessed = ""
        self._lives = 0

    def get_lives_left(self):
        """Gets a response for the player. Whether letter was correct or not.
        
        Args:
            self (Jumper): an instance of Jumper.
            
        Returns:
            string: a reponse for the player.
        """
        if self._letter in self._word:
            self._lives = 0
        elif self._letter not in self._word:
            self._lives += 1
        
        if self._lives == 0:
            return """
        /`~~~~~~~~`\ 
        \_,_,_,_,_,/ 
         \        / 
          \      / 
           |    | 
        \ ( ^.^ ) / 
            )  ) 
            /  \ """
        elif self._lives == 1:
            return """
        \_,_,_,_,_,/
         \        /
          \      /
           |    |
        \ (‘’*.*`) /
            )  )
            /  \ """
        elif self._lives == 2:
            return """  
         \        /
          \      /
           |    |
        \ (‘*.*``) /
            )  )
            /  \ """
        elif self._lives == 3:
            return """
          \      /
           |    |
        \ (``>.< ) /
           )  )
           /  \ """
        elif self._lives == 4:
            return """
           |    |
        \ (`O_O ) /
            )  )
            /  \ """
        elif self._lives == 5:
            return """
        ( x_x )
        / )  ) \ 
          /  \ """

    def is_guessed(self):
        """Whether or not the word is correctly guessed.
        
        Args:
            self (Player): an instance of Player.
            
        Returns:
            boolean: True if the word is guessed; False if not.
        """
        return (self._word == self._letter)

    def watch_word(self, player):
        """Watches the hidden word, keeping track of letters and blanks.
        
        Args:
            self (Jumper): an instance of Jumper.
            letter (string): a given letter.
        """
        for self._letter in list(self._word):
            if self._letter in player.get_letters():
                word = self._letter
            else:
                word = " _ "
            print(word, end="")
            self._guessed += word
        return  self._guessed