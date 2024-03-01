from tinydb import TinyDB

db = TinyDB('../datas/data.json')


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
        sendDatas = {
            "Name": self.player.name,
            "Surname": self.player.surname,
            "Birth Date": self.player.birthDate,
        }
        db.insert({'Players': sendDatas})

    @staticmethod
    def deserialize():

        retrieveDatas = []

        for item in db:
            if 'Players' in item:
                playerList = item['Players']
                data = {
                    "Name": playerList['Name'],
                    "Surname": playerList['Surname'],
                    "Birth Date": playerList['Birth Date'],
                }
                retrieveDatas.append(data)

        return retrieveDatas

