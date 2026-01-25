from environment.card import Card
import random

class Deck:
    def __init__(self):
        self.suits: list = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.faces: list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values: list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.deck: list = []


    def reset(self) -> None:
        """
        This resets the current deck to an unshuffled and complete state.
        """
        self.deck = []
        for suit in self.suits:
            for card in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[card], self.values[card], self.faces[card] == "Ace"))


    def shuffle(self) -> None:
        """
        Shuffles deck.
        """
        random.shuffle(self.deck)


    def draw_card(self) -> Card:
        """
        Pops the top card of the deck and returns it.
        :return: A card instance.
        """
        return self.deck.pop()