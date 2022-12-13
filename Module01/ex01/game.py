class GotCharacter:

    def __init__(self, first_name, is_alive=True):
        self.is_alive = is_alive
        self.first_name = first_name


class Stark(GotCharacter):
    """A class representing the Stark Family. Or when bad things happen to good people"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
