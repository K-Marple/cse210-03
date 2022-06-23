class TerminalService:
    """A service that handles terminal operations. It provides input and output 
    operations for the terminal.
    """

    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with given prompt.
        
        Args:
            self (TerminalService): an instance of TerminalService.
            prompt (string): the prompt to display on the terminal.
        
        Returns:
            string: the user's input as text.
        """
        return input(prompt)

    def read_letter(self, prompt):
        """Gets letter input from the terminal. Directs the user with given prompt.
        
        Args:
            self (TerminalService): an instance of TerminalService.
            prompt (string): The prompt to display on the terminal.
        
        Returns:
            string: the user's input as string.
        """
        return input(prompt)

    def write_text(self, text):
        """Displays given text on the terminal.
        
        Args:
            self (TerminalService): an instance of TerminalService.
            text (sting): the text to display.
        """
        print(text)