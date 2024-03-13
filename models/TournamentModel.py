class MainTournament:
    def __init__(self, name, place, start_date, end_date, round_total, current_round, round_list, player_list,
                 description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_total = round_total
        self.current_round = current_round
        self.all_rounds_list = round_list
        self.player_list = player_list
        self.description = description

