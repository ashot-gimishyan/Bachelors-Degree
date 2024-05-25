class Card:

    values = {
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A',
    }

    suits = {
        1: '\u2665',
        2: '\u2666',
        3: '\u2660',
        4: '\u2663'
    }

    def __init__(self, suit, value):
        self.__value = value
        self.__suit = suit

    def get_card_name(self):
        return '{} of {}'.format(
            Card.values.get(self.__value),
            Card.suits.get(self.__suit)
        )

    def get_card_value(self):
        if 2 <= self.__value <= 9:
            return self.__value
        elif 10 <= self.__value <= 13:
            return 10
        else:
            return 11

    def get_value(self):
        return self.__value

    def get_suit(self):
        return self.__suit

    def __str__(self):
        return '{}{}'.format(
            Card.values.get(self.__value),
            Card.suits.get(self.__suit)
        )


class CardDeck:

    def __init__(self):
        self.__deck = set(Card(y, x) for y in range(1, 5) for x in range(2, 15))

    def __str__(self):
        return ' '.join([card.__str__() for card in self.__deck])

    def deal_card(self):
        if not self.deck_is_empty():
            return self.__deck.pop()
        else:
            raise IndexError('Error! Deck is empty!')

    def deck_is_empty(self):
        if len(self.__deck) == 0:
            return True
        return False


class Player:

    def __init__(self, name, money):
        self.__name = name
        self.__money = money
        self.__hand = []
        self.__hand_score = 0

    def take_card(self):
        card = self.__deck.deal_card()
        self.__hand.append(card)
        self.__hand_score += card.get_card_value()
        if self.__hand_score > 21 and card.get_card_value() == 11:
            self.__hand_score -= 10

    def take_pair(self):
        self.take_card()
        self.take_card()

    def throw_hand(self):
        self.__hand.clear()
        self.__hand_score = 0

    def get_hand(self):
        return ' '.join([card.__str__() for card in self.__hand])

    def get_hand_count(self):
        return len(self.__hand)

    def set_deck(self, deck):
        self.__deck = deck

    def get_name(self):
        return self.__name

    def get_bank(self):
        return self.__money

    def change_balance(self, bet):
        self.__money += bet

    def get_score(self):
        return self.__hand_score