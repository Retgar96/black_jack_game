# from card import Card
import random

class Deck:

    def __init__(self, count_deck):
        self.count_deck = count_deck
        self.cards = {'A_CH': 1 * self.count_deck,
                      'A_BY': 1 * self.count_deck,
                      'A_KR': 1 * self.count_deck,
                      'A_PI': 1 * self.count_deck,

                      'TWO_CH': 1 * self.count_deck,
                      'TWO_BY': 1 * self.count_deck,
                      'TWO_KR': 1 * self.count_deck,
                      'TWO_PI': 1 * self.count_deck,

                      'THREE_CH': 1 * self.count_deck,
                      'THREE_BY': 1 * self.count_deck,
                      'THREE_KR': 1 * self.count_deck,
                      'THREE_PI': 1 * self.count_deck,

                      'FOUR_CH': 1 * self.count_deck,
                      'FOUR_BY': 1 * self.count_deck,
                      'FOUR_KR': 1 * self.count_deck,
                      'FOUR_PI': 1 * self.count_deck,

                      'FIVE_CH': 1 * self.count_deck,
                      'FIVE_BY': 1 * self.count_deck,
                      'FIVE_KR': 1 * self.count_deck,
                      'FIVE_PI': 1 * self.count_deck,

                      'SIX_CH': 1 * self.count_deck,
                      'SIX_BY': 1 * self.count_deck,
                      'SIX_KR': 1 * self.count_deck,
                      'SIX_PI': 1 * self.count_deck,

                      'SEVEN_CH': 1 * self.count_deck,
                      'SEVEN_BY': 1 * self.count_deck,
                      'SEVEN_KR': 1 * self.count_deck,
                      'SEVEN_PI': 1 * self.count_deck,

                      'EIGHT_CH': 1 * self.count_deck,
                      'EIGHT_BY': 1 * self.count_deck,
                      'EIGHT_KR': 1 * self.count_deck,
                      'EIGHT_PI': 1 * self.count_deck,

                      'NINE_CH': 1 * self.count_deck,
                      'NINE_BY': 1 * self.count_deck,
                      'NINE_KR': 1 * self.count_deck,
                      'NINE_PI': 1 * self.count_deck,

                      'TEN_CH': 1 * self.count_deck,
                      'TEN_BY': 1 * self.count_deck,
                      'TEN_KR': 1 * self.count_deck,
                      'TEN_PI': 1 * self.count_deck,

                      'JACK_CH': 1 * self.count_deck,
                      'JACK_BY': 1 * self.count_deck,
                      'JACK_KR': 1 * self.count_deck,
                      'JACK_PI': 1 * self.count_deck,

                      'QUEEN_CH': 1 * self.count_deck,
                      'QUEEN_BY': 1 * self.count_deck,
                      'QUEEN_KR': 1 * self.count_deck,
                      'QUEEN_PI': 1 * self.count_deck,

                      'KING_CH': 1 * self.count_deck,
                      'KING_BY': 1 * self.count_deck,
                      'KING_KR': 1 * self.count_deck,
                      'KING_PI': 1 * self.count_deck}

    def delete_card(self, card_name):
        if self.cards[card_name] > 0:
            if self.cards[card_name] == 1:
                self.cards.pop(card_name)
            else:
                self.cards[card_name] -= 1
        else:
            print('Ошибка: Этой карты нет в колоде.')

    def get_deck(self):
        return self.cards

    def get_card(self):
        try:
            key = random.choice(list(self.cards.keys()))
            self.delete_card(key)
            return key
        except IndexError:
            return 'Колода пуста'







    #     A_CH = Card('A', 'CH', self.count_deck)
    #     A_BY = Card('A', 'BY', self.count_deck)
    #     A_KR = Card('A', 'KR', self.count_deck)
    #     A_PI = Card('A', 'PI', self.count_deck)
    #
    #     TWO_CH = Card('TWO', 'CH', self.count_deck)
    #     TWO_BY = Card('TWO', 'BY', self.count_deck)
    #     TWO_KR = Card('TWO', 'KR', self.count_deck)
    #     TWO_PI = Card('TWO', 'PI', self.count_deck)
    #
    #     THREE_CH = Card('THREE', 'CH', self.count_deck)
    #     THREE_BY = Card('THREE', 'BY', self.count_deck)
    #     THREE_KR = Card('THREE', 'KR', self.count_deck)
    #     THREE_PI = Card('THREE', 'PI', self.count_deck)
    #
    #     FOUR_CH = Card('FOUR', 'CH', self.count_deck)
    #     FOUR_BY = Card('FOUR', 'BY', self.count_deck)
    #     FOUR_KR = Card('FOUR', 'KR', self.count_deck)
    #     FOUR_PI = Card('FOUR', 'PI', self.count_deck)
    #
    #     FIVE_CH = Card('FIVE', 'CH', self.count_deck)
    #     FIVE_BY = Card('FIVE', 'BY', self.count_deck)
    #     FIVE_KR = Card('FIVE', 'KR', self.count_deck)
    #     FIVE_PI = Card('FIVE', 'PI', self.count_deck)
    #
    #     SIX_CH = Card('SIX', 'CH', self.count_deck)
    #     SIX_BY = Card('SIX', 'BY', self.count_deck)
    #     SIX_KR = Card('SIX', 'KR', self.count_deck)
    #     SIX_PI = Card('SIX', 'PI', self.count_deck)
    #
    #     SEVEN_CH = Card('SEVEN', 'CH', self.count_deck)
    #     SEVEN_BY = Card('SEVEN', 'BY', self.count_deck)
    #     SEVEN_KR = Card('SEVEN', 'KR', self.count_deck)
    #     SEVEN_PI = Card('SEVEN', 'PI', self.count_deck)
    #
    #     EIGHT_CH = Card('EIGHT', 'CH', self.count_deck)
    #     EIGHT_BY = Card('EIGHT', 'BY', self.count_deck)
    #     EIGHT_KR = Card('EIGHT', 'KR', self.count_deck)
    #     EIGHT_PI = Card('EIGHT', 'PI', self.count_deck)
    #
    #     NINE_CH = Card('NINE', 'CH', self.count_deck)
    #     NINE_BY = Card('NINE', 'BY', self.count_deck)
    #     NINE_KR = Card('NINE', 'KR', self.count_deck)
    #     NINE_PI = Card('NINE', 'PI', self.count_deck)
    #
    #     TEN_CH = Card('TEN', 'CH', self.count_deck)
    #     TEN_BY = Card('TEN', 'BY', self.count_deck)
    #     TEN_KR = Card('TEN', 'KR', self.count_deck)
    #     TEN_PI = Card('TEN', 'PI', self.count_deck)
    #
    #     JACK_CH = Card('JACK', 'CH', self.count_deck)
    #     JACK_BY = Card('JACK', 'BY', self.count_deck)
    #     JACK_KR = Card('JACK', 'KR', self.count_deck)
    #     JACK_PI = Card('JACK', 'PI', self.count_deck)
    #
    #     QUEEN_CH = Card('QUEEN', 'CH', self.count_deck)
    #     QUEEN_BY = Card('QUEEN', 'BY', self.count_deck)
    #     QUEEN_KR = Card('QUEEN', 'KR', self.count_deck)
    #     QUEEN_PI = Card('QUEEN', 'PI', self.count_deck)
    #
    #     KING_CH = Card('KING', 'CH', self.count_deck)
    #     KING_BY = Card('KING', 'BY', self.count_deck)
    #     KING_KR = Card('KING', 'KR', self.count_deck)
    #     KING_PI = Card('KING', 'PI', self.count_deck)
