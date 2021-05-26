import random

class Sequence:
    """A designated playing surface. The responsibility of Sequence is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Sequence): an instance of Sequence.
        """
        self._piles = []
        self._prepare()

    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Sequence): an instance of Sequence.
            move (Move): The move to apply.
        """
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)
    
    def is_empty(self):
        """Determines if all the stones have been removed from the Sequence.
        
        Args:
            self (Sequence): an instance of Sequence.

        Returns:
            boolean: True if the Sequence has no stones on it; false if otherwise.
        """
        empty = [0] * len(self._piles)
        return self._piles == empty

    def to_string(self):
        """Converts the Sequence data to its string representation.

        Args:
           self (Sequence): an instance of Sequence.

        Returns:
            string: A representation of the current Sequence.
        """ 
        text =  "\n--------------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n--------------------"
        return text

    def _prepare(self):
        """Sets up the Sequence with a random number of piles containing a random 
        number of stones.
        
        Args:
            self (Sequence): an instance of Sequence.
        """
        piles = random.randint(2, 5) 
        for n in range(piles):
            stones = random.randint(1, 9)
            self._piles.append(stones)