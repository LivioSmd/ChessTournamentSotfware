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

    @staticmethod
    def RetrievePlayerInfo():
        while True:
            while True:
                input_name_value = input("\nEnter player's Name: ").strip()
                if input_name_value.isdigit():
                    print(f'"{input_name_value}" is not a valid Name.')
                else:
                    while True:
                        input_surname_value = input("Enter player's Surname: ").strip()
                        if input_surname_value.isdigit():
                            print(f'"{input_surname_value}" is not a valid Surname.')
                        else:
                            while True:
                                input_date_value = input("Enter the player's Birth Date (DD/MM/YYYY): ").strip()
                                if not re.match(r'^\d{2}/\d{2}/\d{4}$', input_date_value):
                                    print(f'"{input_date_value}" is not a valid Birth Date.')
                                else:
                                    print(
                                        f"\n---- New player Registered : {input_name_value} {input_surname_value} {input_date_value} ! ----\n")
                                    return {
                                        "name": input_name_value,
                                        "surname": input_surname_value,
                                        "birthDate": input_date_value,
                                    }

    @staticmethod
    def DisplayDataBase(data):
        for player in data:
            print(f'{player}')
