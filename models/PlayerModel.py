from tinydb import TinyDB

db = TinyDB('../datas/data.json')
players_table = db.table('players')


class PlayerModel:
    def __init__(self, name=None, surname=None, birthDate=None):
        self.id = -1
        self.name = name
        self.surname = surname
        self.birthDate = birthDate
        self.score = 0

    def __str__(self):
        return f"{self.id}. {self.name} {self.surname} score: {self.score}"

    def __repr__(self):
        return f"{self.id}. {self.name} {self.surname} score: {self.score}"

    def serialize(self):
        player_serialized = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birthDate": self.birthDate,
            "score": self.score,
        }
        return player_serialized

    def deserialize(self, player):
        self.id = player.get('id')
        self.name = player.get('name')
        self.surname = player.get('surname')
        self.birthDate = player.get('birthDate')
        self.score = player.get('score')
        return self

    def insert_player_in_db(self):
        self.id = players_table.insert(self.serialize())
        self.update()

    def update(self):
        players_table.update(self.serialize(), doc_ids=[self.id])

    def player_retrieval(self, id):
        player = db.table('players').get(doc_id=id)
        return self.deserialize(player)

    @staticmethod
    def retrieve_all_players_from_db():
        players_list = []
        for player in players_table.all():
            players_list.append(PlayerModel().deserialize(player))

        return players_list
