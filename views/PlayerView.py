import re


class PlayerView:

    @staticmethod
    def UserChoice():
        while True:
            print('1. Add a player')
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

    @staticmethod
    def RetrievePlayerInfo():
        while True:
            while True:
                input_name_value = input("enter player's name: ").strip()
                if input_name_value.isdigit():
                    print(f'"{input_name_value}" is not a valid name.')
                else:
                    while True:
                        input_surname_value = input("enter player's surname: ").strip()
                        if input_surname_value.isdigit():
                            print(f'"{input_surname_value}" is not a valid surname.')
                        else:
                            while True:
                                input_date_value = input("enter the player's birth date (DD/MM/YYYY): ").strip()
                                if not re.match(r'^\d{2}/\d{2}/\d{4}$', input_date_value):
                                    print(f'"{input_date_value}" is not a valid date.')
                                else:
                                    print(
                                        f"New player Registered ---> {input_name_value} {input_surname_value} {input_date_value} !")
                                    return {
                                        "name": input_name_value,
                                        "surname": input_surname_value,
                                        "birthDate": input_date_value,
                                    }

    @staticmethod
    def DisplayDataBase(data):
        for index, player in enumerate(data):
            print(f'{index}. {player}')
        print('-------------------------')