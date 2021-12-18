class GameTable:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        print('game table created')

    def get_hand_players(self):
        for player in self.players:
            hand = {1: self.deck.get_card(), 2: self.deck.get_card()}
            player.hand = hand
        return self.players

    def calculate_score_card(self):
        for player in self.players:
            player.score = 1
