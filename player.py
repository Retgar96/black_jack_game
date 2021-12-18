class Player:
    def __init__(self, bank, name, hand, score=0):
        self.bank = bank
        self.name = name
        self.status = True
        self.hand = hand
        self.score = score
        print('player: ', self.name, 'created')

    def minus_bank(self, value):
        if self.bank >= value and self.status:
            self.bank -= value
        else:
            self.bank -= value
            self.status = False
            print(self.name, ' проиграл всю зарплату')

    def plus_bunk(self, value):
        self.bank += value

    def clear_hand(self):
        self.hand = {}
