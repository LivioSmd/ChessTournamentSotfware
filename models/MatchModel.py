class MatchModel:

    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b

    def match(self):

        player_match = (
            [self.player_a, 0],
            [self.player_b, 0]
        )

        return player_match