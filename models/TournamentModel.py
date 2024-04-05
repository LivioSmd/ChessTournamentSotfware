from tinydb import TinyDB

db = TinyDB('../datas/data.json')
tournaments_table = db.table('tournaments')


class TournamentModel:
    def __init__(self, name, place, start_date, end_date, round_total, current_round, all_round_list, description,
                 player_list):
        self.id = -1
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_total = round_total
        self.current_round = current_round
        self.all_rounds_list = all_round_list
        self.description = description
        self.player_list = player_list

    def serialize(self):
        tournament_serialized = {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "startDate": self.start_date,
            "startEnd": self.end_date,
            "totalRound": self.round_total,
            "currentRound": self.current_round,
            "allRoundsList": self.all_rounds_list,
            "description": self.description,
            "playerList": [p.id for p in self.player_list],
        }

        players = []
        for p in self.player_list:
            players.append(p.id)

        return tournament_serialized

    def insert_tournament_in_db(self):
        self.id = tournaments_table.insert(self.serialize())
        self.update()

    def update(self):
        tournaments_table.update(self.serialize(), doc_ids=[self.id])
