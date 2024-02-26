

class MainView:

    @staticmethod
    def UserChoice():
        while True:
            print('1. Add a player')
            print('2. Quit')
            input_choice_value = int(input('Make your choice: '))
            if input_choice_value == 1 or input_choice_value == 2:
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')

    @staticmethod
    def RecapPlayerRegistered(player):
        print(f"New player Registered ! ---> {player["Name"]} {player["Surname"]} {player["Birth Date"]}")

    @staticmethod
    def EndProgram():
        return print('Program out.')

    @staticmethod
    def RetrieveName():
        while True:
            input_name_value = input("enter player's name:")
            if input_name_value.isdigit():
                print(f'{input_name_value} is not a valid name')
            else:
                return input_name_value

    @staticmethod
    def RetrieveSurname():
        while True:
            input_surname_value = input("enter player's surname:")
            if input_surname_value.isdigit():
                print(f'{input_surname_value} is not a valid surname')
            else:
                return input_surname_value

    @staticmethod
    def RetrieveBirthDate():
        input_date_value = input("enter the player's birth date (MM/dd/YYYY):")
        return input_date_value