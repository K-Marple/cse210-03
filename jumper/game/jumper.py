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
        self._word = random.randint(word_list)
        self._parachute = "pass"

    def get_response(self):
        """Gets a response for the player. Whether letter was correct or not.
        
        Args:
            self (Jumper): an instance of Jumper.
            
        Returns:
            string: a reponse for the player.
        """
        reponse = "(^.^) Getting ready."
        pass

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
        pass