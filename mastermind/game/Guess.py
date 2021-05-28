class Guess():
    """A guess and corresponding hint in the game. The responsibility of Guess is to keep track of the guess and compare it to the actual
            number to create an appropriate hint.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (str): The player's guess.
        _hint (str): The hint calculated according to the rules of the game.
        _current_player (str): The player who made the guess
        _number (str): The number that must be found
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = ""
        self._number = ""
        self._hint = ""

    def get_guess(self):
        """Returns the player's current guess.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._guess

    def get_hint(self):
        """Returns the stored hint.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._hint

    def make_hint(self):
        """Returns the calculated guess according to the rules of Mastermind

        Args:
            self (Guess): an instance of Guess.
            guess (str): The players current guess
        """
        hint = ""
        guess = self._guess
        number = self._number

        # Convert parameters into string format
        if type(guess) != str:
            guess = str(guess)
        if type(number) != str:
            number = str(number)
        
        for i in range(len(guess)):     # Adaptable if a number other than four digits is used
            if guess[i] == number[i]:   # If the number is correct and in the right place.
                hint += "x"
            elif guess[i] in number:    # If the number is correct but in the wrong place.
                hint += "o"
            else:                       # If the number is incorrect.
                hint += "*"

        self._hint = hint
