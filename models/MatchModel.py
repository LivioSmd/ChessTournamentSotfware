class MatchModel:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b

    def __str__(self):
        return f"{self.player_a} {self.player_b} kkkkkkk"

    def __repr__(self):
        return f"{self.player_a} {self.player_b} kkkkkkkk"

    def match(self):
        player_match = (
            [self.player_a, 0],
            [self.player_b, 0]
        )
        return player_match
