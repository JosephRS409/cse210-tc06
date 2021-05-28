from game.Sequence import Sequence
from game.Console import Console
from game.Guess import Guess
from game.Player import Player
from game.Roster import Roster


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._sequence = Sequence()
        self._guess = Guess()
        self._console = Console()
        self._player = Player()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()
        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        start_message = "\nWelcome to Mastermind!\n"
        instructions = ("""Instructions: 
        The players take turns guessing the secret code based on the hint that is offered.
        An x means a correct number in a correct position. An o means a correct number in 
        an incorrect position. An * means an incorrect number.\n""")

        self._console.write(start_message)
        self._console.write(instructions)
        self._sequence._generate() # calls the function to generate the sequence

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = self._player.name = name
            self._roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.
        Args:
            self (Director): An instance of Director.
        """
        #sets the sequences for the players
        number = self._sequence.sequence_one

        # get next player's move
        self._player.name = self._roster.get_current()
        self._console.write(f"{self._player.get_name()}'s turn:")
        
        # Gets input from the user
        guess = self._console.read_number(f"Guess what the {self._sequence.get_num_length()} digit number is! ", self._sequence.get_num_length())
        self._guess._number = number # sets the number in the guess class
        self._guess._guess = guess # sets the guess in the guess class
        self._guess.make_hint() # makes the hint for the player
        player_guess = self._guess._guess # sets the move to the guess
        self._player.set_move(player_guess)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.
        Args:
            self (Director): An instance of Director.
        """
        if str(self._player.get_move()).upper() == str(self._sequence.sequence_one): # Checks to see if the sequence and the guess are the same
            winner = self._roster.get_current() #Gets the winners name
            name = winner
            print(f"\n{name} won!")
            self._keep_playing = False # ends the game
        else:
            print(self._guess.get_hint()) # prints the hint for the players
            self._roster.next_player() # goes to the next player.
