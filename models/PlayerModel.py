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

