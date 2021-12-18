from re import split


class calculate_score():
    def __init__(self, player):
        self.player = player

        var = {'A': 11,
               'TWO': 2,
               'THREE': 3,
               'FOUR': 4,
               'FIVE': 5,
               'SIX': 6,
               'SEVEN': 7,
               'EIGHT': 8,
               'NINE': 9,
               'TEN': 10,
               'JACK': 10,
               'QUEEN': 10,
               'KING': 10,
               }

    def get_score(self):
        hand = self.player.hand
        score = hand[1]['score'] + hand[2]['score']
        self.player.score = score
