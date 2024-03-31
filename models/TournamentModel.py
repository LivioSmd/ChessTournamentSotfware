from tinydb import TinyDB

db = TinyDB('../datas/data.json')
tournaments_table = db.table('tournaments')


class MainTournament:
    def __init__(self, id, name, place, start_date, end_date, round_total, current_round, all_round_list, description,
                 player_list):
        self.id = id
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_total = round_total
        self.current_round = current_round
        self.all_rounds_list = all_round_list
        self.description = description
        self.player_list = player_list


class ManageTournament:
    def __init__(self, tournament):
        self.tournament = tournament

    def serialize(self):
        tournament_serialized = {
            "id": self.tournament.id,
            "name": self.tournament.name,
            "place": self.tournament.place,
            "startDate": self.tournament.start_date,
            "startEnd": self.tournament.end_date,
            "totalRound": self.tournament.round_total,
            "currentRound": self.tournament.current_round,
            "allRoundsList": self.tournament.all_rounds_list,
            "description": self.tournament.description,
            "playerList": self.tournament.player_list,
        }
        return tournament_serialized

    @staticmethod
    def insert_tournament_in_db(tournament):
        """Insert tournament in database as dictionary"""
        ManageTournament.update_tournament_id(tournaments_table.insert(tournament))

    @staticmethod
    def update_tournament_id(tournament_id_in_db):
        tournaments_table.update({'id': tournament_id_in_db}, doc_ids=[tournament_id_in_db])
