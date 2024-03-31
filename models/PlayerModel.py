from tinydb import TinyDB

db = TinyDB('../datas/data.json')
players_table = db.table('players')


class PlayerModel:
    def __init__(self, name, surname, birthDate):
        self.id = -1
        self.name = name
        self.surname = surname
        self.birthDate = birthDate

    def __str__(self):
        return f"{self.id}. {self.name} {self.surname}"

    def __repr__(self):
        return f"{self.id}. {self.name} {self.surname}"

    def serialize(self):
        player_serialized = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birthDate": self.birthDate,
        }
        return player_serialized

    def deserialize(self, player):
        self.id = player.get('id')
        self.name = player.get('name')
        self.surname = player.get('surname')
        self.birthDate = player.get('birthDate')
        return self

    def insert_player_in_db(self):
        player = self.serialize()
        insert_id = players_table.insert(player)
        self.update(insert_id)

    @staticmethod
    def retrieve_all_players_from_db():     # TODO voir pour enlever le static
        all_players = players_table.all()

        players_list = []
        for player in all_players:
            player_instance = PlayerModel("", "", "")
            players_list.append(player_instance.deserialize(player))

        return players_list

    @staticmethod
    def update(player_id_in_db):
        players_table.update({'id': player_id_in_db}, doc_ids=[player_id_in_db])
