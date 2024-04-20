from tinydb import TinyDB
from models.PlayerModel import PlayerModel

db = TinyDB('../datas/data.json')
tournaments_table = db.table('tournaments')


class TournamentModel:
    def __init__(self, name=None, place=None, start_date=None, end_date=None, round_total=None,
                 description=None, player_list=None):
        self.id = -1
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_total = round_total
        self.current_round = 1
        self.all_rounds_list = []
        self.description = description
        self.player_list = player_list

    def __str__(self):
        return f"{self.name}. from: {self.start_date} to: {self.end_date} and {self.current_round} and {self.all_rounds_list}"

    def __repr__(self):
        return f"{self.name}. from: {self.start_date} to: {self.end_date} and {self.current_round} and {self.all_rounds_list}"

    def serialize(self):
        tournament_serialized = {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "totalRound": self.round_total,
            "currentRound": self.current_round,
            "allRoundsList": self.all_rounds_list,
            "description": self.description,
            "playerList": [p.id for p in self.player_list],
        }

        """"
        players = []
        for p in self.player_list:
            players.append(p.id)
        """""

        return tournament_serialized

    def deserialize(self, tournament):
        self.id = tournament.get('id')
        self.name = tournament.get('name')
        self.place = tournament.get('place')
        self.start_date = tournament.get('startDate')
        self.end_date = tournament.get('endDate')
        self.round_total = tournament.get('totalRound')
        self.current_round = tournament.get('currentRound')
        self.all_rounds_list = tournament.get('allRoundsList')
        self.description = tournament.get('description')
        self.player_list = [PlayerModel().player_retrieval(p) for p in tournament.get('playerList')]

        """"
        players = []
        for p in tournament.get('playerList'):
            players.append(PlayerModel().player_retrieval(p))
        """""

        return self

    def insert_tournament_in_db(self):
        self.id = tournaments_table.insert(self.serialize())
        self.update()

    def update(self):
        tournaments_table.update(self.serialize(), doc_ids=[self.id])

    def tournament_retrieval(self, id):
        tournament = db.table('tournaments').get(doc_id=id)
        return self.deserialize(tournament)
