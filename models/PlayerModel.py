from tinydb import TinyDB

db = TinyDB('../datas/data.json')
players_table = db.table('players')
players_with_index = players_table.all()


class PlayerModel:
    def __init__(self, name, surname, birthDate):
        self.name = name
        self.surname = surname
        self.birthDate = birthDate

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"{self.name} {self.surname}"


class ManagePlayer:
    def __init__(self, player):
        self.player = player

    def serialize(self):
        """ Recover a player instance /  Returns a dictionary containing player information"""
        player_serialized = {
            "name": self.player.name,
            "surname": self.player.surname,
            "birthDate": self.player.birthDate,
        }

        return player_serialized

    @staticmethod
    def deserialize(a_player):
        return PlayerModel(a_player.get("name"), a_player.get("surname"), a_player.get("birthDate"))

    @staticmethod
    def insert_player_in_db(player):
        """Insert players in database as dictionary"""
        players_table.insert(player)

    @staticmethod
    def retrieve_all_players_from_db():
        """Returns a list of all players in the database"""
        all_players = players_table.all()

        players_list = []
        for player in all_players:
            players_list.append(ManagePlayer.deserialize(player))

        return players_list
