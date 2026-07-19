import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "Jack", "Queen", "King", "Ace"]

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

def deal_hand(deck):
    hand = []

    for i in range(5):
        hand.append(deck.deal_card())

    return hand

def display_hand(hand):
    print("\nYour Hand:")
    for i in range(len(hand)):
        print(f"{i + 1}. {hand[i]}")

def replace_cards(hand, deck):
    choice = input(
        "\nEnter card numbers to replace (example: 1 3 5)\n"
        "Press Enter to keep all cards: "
    ).strip()

    if choice == "":
        return

    positions = choice.split()

    for pos in positions:
        if pos.isdigit():
            index = int(pos) - 1
            if 0 <= index < 5:
                hand[index] = deck.deal_card()

def main():
    print("Card Draw Game")

    deck = Deck()

    hand = deal_hand(deck)

    print("\nStarting Hand")
    display_hand(hand)

    replace_cards(hand, deck)

    print("\nFinal Hand")
    display_hand(hand)

main()