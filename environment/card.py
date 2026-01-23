class Card:
    def __init__(self, suit, face, value, is_ace):
        self.suit: str = suit
        self.face: str = face
        self.value: int = value
        self.is_ace: bool = is_ace


    def __str__(self):
        return f"{self.face} of {self.suit}"