import re


class PlayerView:

    def RetrievePlayerInfo(self):
        return {
            "name": self.getString("\nEnter player's Name:"),
            "surname": self.getString("Enter player's Surname:"),
            "birthDate": self.getDate("Enter player's Birth Date:"),
        }

    @staticmethod
    def getString(message):
        while True:
            input_value = input(message).strip()
            if input_value.isdigit():
                print(f'"{input_value}" is not valid')
            else:
                return input_value

    @staticmethod
    def getDate(message):
        while True:
            input_value = input(message).strip()
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', input_value):
                print(f'"{input_value}" is not valid (dd/mm/yyyy)')
            else:
                return input_value

    @staticmethod
    def DisplayDataBase(data):
        for player in data:
            print(f'{player}')

    @staticmethod
    def DisplayPlayer(player):
        print(player)