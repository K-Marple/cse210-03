from game.terminal_service import TerminalService
from game.player import Player
from game.jumper import Jumper
import random

class Director:
    """A person who directs the game. They control the different parts of the game.
    
    Attributes:
        player (Player): The person playing the game.
        continue_playing (boolean): Whether or not the player is still playing.
        jumper (Jumper): The game's jumper, parachuter.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._player = Player()
        self._continue_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._guess = []

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # word_list = ["chemistry", "song", "friendship", "science", "volume", "gate", "literature",
        #     "philosophy", "construction", "area", "difficulty", "vehicle", "chest", "aspect", 
        #     "percentage", "agency", "grocery", "girlfriend", "hair", "basket", "length", "equipment", 
        #     "camera", "wedding", "party"]
        # self._word = random.choice(word_list)
        # for self._letter in list(self._word):
            # print(" _ ", end="")
        while self._continue_playing:
            print()
            self._get_inputs()
            print()
            self._do_updates()
            print()
            self._do_outputs()

    def _get_inputs(self):
        """Gets letter from the player.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper.watch_word(self._player)
        self._guess = self._terminal_service.read_letter("\nGuess a letter (a-z): ")
        self._player.add_letters(self._guess)
        

    def _do_updates(self):
        """Keeps track of guessed letter.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper.watch_word(self._player)
        # for self._letter in self._word:
        #     self._word.append("_")
        #     print(self._word)
        #     # if self._guess in self._word:
        #     #     print(self._guess, end="")
        #     # else:
        #     #     print(" _ ", end="")

    def _do_outputs(self):
        """Adds guessed letter to word or clears a part of the chute.
        
        Args:
            self (Director): an instance of Director.
        """
        lives = self._jumper.get_lives_left()
        self._terminal_service.write_text(lives)
        if self._jumper.is_guessed():
            self._continue_playing = False