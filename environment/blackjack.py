from environment.deck import Deck
from environment.hand import Hand
import random

class Blackjack:
    def __init__(self):
        self.deck: Deck  = Deck()
        self.queue: list = []


    def next_hand(self) -> tuple:
        """
        Creates a new hand or plays the next hand if the original hand was split by using the init_hand() function.
        :return: a state-tuple containing the player's hand value, the house's card, if you have an ace and if the hand is splittable.
        """
        if len(self.queue) > 0:
            hand = self.queue.pop()
            self.init_hand(hand)

        else:
            self.init_hand()

        return self.state


    def init_hand(self, hand=None) -> None:
        """
        This function is connected to the next_hand function and creates the hands according to the demand. If you want a new hand you reset and reshuffle
        the deck and add two cards each otherwise after splitting you use the same deck and the player gets only one card.
        :param hand: this parameter is either none at the beginning of a hand or is a hand with two cards if the function is used after splitting.
        """
        if hand == None:
            self.player_hand: Hand = Hand()
            self.house_hand: Hand = Hand()

            self.deck.reset()
            self.deck.shuffle()

            for i in range(2):
                card = self.deck.draw_card()
                self.player_hand.add_card(card)

                card = self.deck.draw_card()
                self.house_hand.add_card(card)

        else:
            self.player_hand = hand

        self.player_hand.process()
        self.state = (self.player_hand.value, self.house_hand.hand[0].value, self.player_hand.soft, self.player_hand.double_possible, self.player_hand.splittable)


    def step(self, action: int) -> tuple:
        """
        Here the program evaluates the functions and either plays on or decides to end the game.
        :param action: An integer encoding one of four actions: 0 --> stand, 1 --> hit, 2 --> double, 3 --> split.
        :return: This tuple contains now not only the state, but also the reward and if the hand is over
        """
        reward: float = 0
        hand_over: bool = False
        self.double_possible = False

        if action == 0:
            reward = self.hand_over()
            hand_over = True

        elif action == 1:
            card = self.deck.draw_card()
            self.player_hand.add_card(card)
            self.player_hand.process()
            if self.player_hand.value > 21:
                reward = self.hand_over()
                hand_over = True

        elif action == 2:
            if len(self.player_hand.hand) != 2:
                print("You cannot double down!")

            else:
                self.player_hand.reward = 2
                card = self.deck.draw_card()
                self.player_hand.add_card(card)
                self.player_hand.process()
                reward = self.hand_over()
                hand_over = True

        elif action == 3:
            if not self.state[-1]:
                print("Hand is not splittable!")

            else:
                card1 = self.player_hand.hand[0]
                card2 = self.player_hand.hand[1]

                hand1 = Hand()
                hand2 = Hand()

                hand1.add_card(card1)
                hand2.add_card(card2)

                card = self.deck.draw_card()
                hand1.add_card(card)
                card = self.deck.draw_card()
                hand2.add_card(card)

                hand1.process()
                hand2.process()

                hand1.reward = 1
                hand2.reward = 1

                self.queue.append(hand2)
                self.queue.append(hand1)

                state1 = (hand1.value, self.house_hand.hand[0].value, hand1.soft, hand1.double_possible, hand1.splittable)
                state2 = (hand2.value, self.house_hand.hand[0].value, hand2.soft, hand2.double_possible, hand2.splittable)

                states = (state1, state2)

                return (states, 0, False)

        self.state = (self.player_hand.value, self.house_hand.hand[0].value, self.player_hand.soft, self.player_hand.double_possible, self.player_hand.splittable)
        step_result = (self.state, reward, hand_over)

        return step_result


    def hand_over(self) -> float:
        """
        The game is evaluated and the winner gets decided.
        :return: The reward is a number that decides how "good" the player played the game. It normally is either -1 for a loss, 0 for a draw and 1 for a win. However, the values can double if the player decides to double down.
        """
        reward: float = 0
        self.house_hand.finish(self.deck)
        if self.player_hand.value > 21:
            reward = -1 * self.player_hand.reward

        elif self.house_hand.value > 21:
            reward = self.player_hand.reward

        elif self.player_hand.value > self.house_hand.value:
            reward = self.player_hand.reward

        elif self.player_hand.value < self.house_hand.value:
            reward = -1 * self.player_hand.reward

        return reward


    def action_random(self, double_possible, splittable):
        action_space = [0, 1]
        if double_possible:
            for i in range(1):
                action_space.append(2)
        if splittable:
            for i in range(1):
                action_space.append(3)
        return random.choice(action_space)
