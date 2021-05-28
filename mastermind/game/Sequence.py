import random as r

class Sequence:
    """A designated playing surface. The responsibility of Sequence is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        sequence_one: A randomly generated number
    """
    import random as r


class Sequence:

    def __init__(self):

        self.sequence_one = ""
        self._num_length = 0

    def _generate(self):
        """self.sequence_one = str(r.randint(1000, 9999)) # Randomly generates a sequence for the player to guess"""
        self._num_length = int(input("How long of a sequence would you like? "))
        sequence = ""
        let_percent = int(input("""How many letters would you like in the sequence?
        1 = None
        2 = Some Letters
        3 = A Healthy Amount
        4 = A Metric Crap Ton
        5 = Alpha-pocalypse\n>"""))

        if let_percent != 5:
            for _ in range(self._num_length):
                letter = r.randint(0, let_percent)
                if letter == 1:
                    num = r.randint(0, 9)
                    sequence = str(num) + sequence
                else:
                    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
                    num = alpha[r.randint(0, 26)-1]
                    sequence = str(num) + sequence

        else:
            for _ in range(self._num_length):
                alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
                num = alpha[r.randint(0, 26)-1]
                sequence = str(num) + sequence

        self.sequence_one = sequence


    def get_num_length(self):
        return self._num_length
