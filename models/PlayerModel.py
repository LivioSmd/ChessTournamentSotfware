from tinydb import TinyDB

db = TinyDB('../datas/data.json')
players_table = db.table('players')


class PlayerModel:
    def __init__(self, name, surname, birthDate):
        self.name = name
        self.surname = surname
        self.birthDate = birthDate

    def Player(self):
        return {
            "Name": self.name,
            "Surname": self.surname,
            "Birth Date": self.birthDate,
        }


class ManagePlayer:
    def __init__(self, player):
        self.player = player

    def serialize(self):
        """ Recover a player instance /  Returns a dictionary containing player information"""
        player_serialized = {
            "Name": self.player.name,
            "Surname": self.player.surname,
            "Birth Date": self.player.birthDate,    #enelever les espaces et maj au debut (verifier)
        }

        return player_serialized

    @staticmethod
    def deserialize(players_list):
        """Recover a list of players / Returns a dictionary containing player-numbered dictionaries"""
        all_players = {}

        for index, player in enumerate(players_list):
            player_info = {
                "Name": player['Name'],
                "Surname": player['Surname'],
                "Birth Date": player['Birth Date'],
            }
            all_players.update({index: player_info})

        return all_players  # doit retourner une instance de classe (prends self et mon instance et retourne une instance)

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
            players_list.append(player) # appel ma deserialise

        return players_list
