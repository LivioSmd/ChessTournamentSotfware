from tinydb import TinyDB

db = TinyDB('../datas/data.json')
players_table = db.table('players')


class PlayerModel:
    def __init__(self, name=None, surname=None, birthDate=None):
        self.id = -1
        self.name = name
        self.surname = surname
        self.birthDate = birthDate

    def __str__(self):
        return f"{self.id}. {self.name} {self.surname}"

    def __repr__(self):
        return f"{self.id}. {self.name} {self.surname}"

    def serialize(self):
        """player serialization"""
        player_serialized = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birthDate": self.birthDate,
        }
        return player_serialized

    def deserialize(self, player):
        """player deserialization"""
        self.id = player.get('id')
        self.name = player.get('name')
        self.surname = player.get('surname')
        self.birthDate = player.get('birthDate')
        return self

    def insert_player_in_db(self):
        """inserting player into the database"""
        self.id = players_table.insert(self.serialize())
        self.update()

    def update(self):
        """update player information"""
        players_table.update(self.serialize(), doc_ids=[self.id])

    def player_retrieval(self, id):
        """retrieve a player from the database"""
        player = db.table('players').get(doc_id=id)
        return self.deserialize(player)

    @staticmethod
    def retrieve_all_players_from_db():
        """retrieve all players from the database"""
        players_list = []
        for player in players_table.all():
            players_list.append(PlayerModel().deserialize(player))

        return players_list
