#from .models import Word

import random

class Puzzle:
    def __init__(self, word):
        self.masked_word = self._hide_letters_(word)

    def _hide_letters_(self,word):
        self.chars = list(word)
        length = len(self.chars)
        # Determine the number of letters to hide (you can adjust this as needed)
        num_letters_to_hide = int(length * 0.5)  # Hiding 30% of the letters

        # Generate random indices to hide letters
        self.indices_to_hide = random.sample(range(length), num_letters_to_hide)

        # Replace the letters at the random indices with the placeholder
        for index in self.indices_to_hide:
            self.chars[index] = "*"

        # Convert the list back to a string
        self.hidden_string = "".join(self.chars)

        return self.hidden_string

puzzle = Puzzle("home")
print(puzzle.masked_word)
