import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt) # This merely reads a prompt and grabs the user's input.

    def read_number(self, prompt, num_length):
        """Gets numerical input from the user through the screen. This is a failsafe to ensure the input is a "number".

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as a number in a string.
        """
<<<<<<< HEAD
        return int(input(prompt)) # Same as before, except with the user entering a number.
=======
        valid = False
        while not valid:
            guess = input(prompt)
            if guess.isalnum() and len(guess) == num_length:       # if all the characters in the input are numbers then the loop breaks and returns the variable
                valid = True
            else:                       # otherwise it displays an error message and loops again.
                print(f"{guess} is not a valid guess, please try again!")

        return guess
>>>>>>> master
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text) # This shows text to the screen/console.