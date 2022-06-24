from terminal_service import TerminalService
from player import Player
from jumper import Jumper

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

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._continue_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets letter from the player.
        
        Args:
            self (Director): an instance of Director.
        """
        new_guess = self._terminal_service.read_letter("\nGuess a letter (a-z): ")
        self._player.add_letters(new_guess)

    def _do_updates(self):
        """Keeps track of guessed letter.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper.watch_chute(self._player)

    def _do_outputs(self):
        """Adds guessed letter to word or clears a part of the chute.
        
        Args:
            self (Director): an instance of Director.
        """
        lives = self._jumper.get_lives_left()
        self._terminal_service.write_text(lives)
        if self._jumper.is_guessed():
            self._continue_playing = False