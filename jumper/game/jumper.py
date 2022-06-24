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
        self._blanks = []

    def get_lives_left(self):
        """Gets a response for the player. Whether letter was correct or not.
        
        Args:
            self (Jumper): an instance of Jumper.
            
        Returns:
            string: a reponse for the player.
        """
        lives = "(^.^) Getting ready."
        full_lives = """/`~~~~~~~~`\ 
        \_,_,_,_,_,/ 
         \        / 
          \      / 
           |    | 
        \ ( ^.^ ) / 
            )  ) 
            /  \ """
        word_list = ["chemistry", "song", "friendship", "science", "volume", "gate", "literature",
            "philosophy", "construction", "area", "difficulty", "vehicle", "chest", "aspect", 
            "percentage", "agency", "grocery", "girlfriend", "hair", "basket", "length", "equipment", 
            "camera", "wedding", "party"]
        word = random(word_list)
        self._word = word.split()


    def is_guessed(self):
        """Whether or not the word is correctly guessed.
        
        Args:
            self (Jumper): an instance of Jumper.
            
        Returns:
            boolean: True if the word is guessed; False if not.
        """
        return (self._word == letters)

    def watch_chute(self):
        """Watches the parachute be keeping track of how long it is.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        blanks = 
        self._blanks.append(blanks)