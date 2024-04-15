import re


class PlayerView:

    @staticmethod
    def UserChoice():
        while True:
            print('\n1. Add a player')
            print('2. Retrieve all players in Data Base')
            print('3. Quit')
            print('4. Launch a Tournament')
            input_choice_value = int(input('Make your choice: '))
            if (input_choice_value == 1
                    or input_choice_value == 2
                    or input_choice_value == 3
                    or input_choice_value == 4):
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')

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