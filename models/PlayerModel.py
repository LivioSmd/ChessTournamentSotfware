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

        send_datas = {
            "Name": self.player.name,
            "Surname": self.player.surname,
            "Birth Date": self.player.birthDate,
        }

        players_table.insert(send_datas)



    @staticmethod
    def deserialize():

        players_list = players_table.all()
        retrieve_datas = []

        for player in players_list:
            data = {
                "Name": player['Name'],
                "Surname": player['Surname'],
                "Birth Date": player['Birth Date'],
            }
            retrieve_datas.append(data)

        return retrieve_datas

