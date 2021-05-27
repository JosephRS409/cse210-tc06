import random as r

class Sequence:
    """A designated playing surface. The responsibility of Sequence is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    import random as r


class Sequence:

    def __init__(self):

        self.sequence_one = ""
        self._generate() # calls the function to generate the sequence

    def _generate(self):
        self.sequence_one = str(r.randint(1000, 9999)) # Randomly generates a sequence for the player to guess
