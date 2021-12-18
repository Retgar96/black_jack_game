class Card:

    def __init__(self, nominal, suit, count_deck):
        self.nominal = nominal
        self.suit = suit
        self.count_card = count_deck

    def get_name_card(self):
        return self.nominal+' '+self.suit

    def delete_card(self):
        if self.count_card > 0:
            self.count_card -= 1
