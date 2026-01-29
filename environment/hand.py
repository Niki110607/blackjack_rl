class Hand:
    def __init__(self):
        self.hand: list = []
        self.value: int = 0
        self.has_ace: bool = False
        self.double_possible: bool = False
        self.splittable: bool = False
        self.reward: float = 1.0
        self.ace_count: int = 0

    def add_card(self, card) -> None:
        """
        Appends a card to a hand.
        """
        self.hand.append(card)


    def process(self) -> None:
        """
        This function computes the hand value, if the function has an ace, if it is splittable and decides if the ace should count 1 or 11.
        """
        self.value = 0
        self.soft = False
        self.splittable = False
        self.ace_count = 0
        self.deductions = 0
        self.double_possible = False
        self.splitted = False

        for card in self.hand:
            self.value += card.value

            if card.is_ace:
                self.has_ace = True
                self.ace_count += 1
        for ace in range(self.ace_count):
            if self.value > 21:
                self.value -= 10
                self.deductions += 1

        if self.ace_count > self.deductions:
            self.soft = True

        if len(self.hand) == 2:
            self.double_possible = True

        if len(self.hand) == 2 and self.hand[0].face == self.hand[1].face:
            self.splittable = True


    def finish(self, deck) -> None:
        """
        After the player stands the house hand gets evaluated.
        :param deck: This is the deck used in the current hand.
        """
        self.process()
        while self.value < 17:
            card = deck.draw_card()
            self.add_card(card)
            self.process()