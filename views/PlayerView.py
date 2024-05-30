import re


class PlayerView:

    def retrieve_player_info(self):
        return {
            "name": self.get_string("\nEnter player's Name: "),
            "surname": self.get_string("Enter player's Surname: "),
            "birthDate": self.get_date("Enter player's Birth Date: "),
        }

    @staticmethod
    def get_string(message):
        while True:
            input_value = input(message).strip()
            if input_value.isdigit():
                print(f'"{input_value}" is not valid')
            else:
                return input_value

    @staticmethod
    def get_date(message):
        while True:
            input_value = input(message).strip()
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', input_value):
                print(f'"{input_value}" is not valid (dd/mm/yyyy)')
            else:
                return input_value

    @staticmethod
    def display_data_base(data):
        sorted_players = sorted(data, key=lambda p: p.name)
        for player in sorted_players:
            print(player)
        return True

    @staticmethod
    def display_player(player):
        print(player)
