class MainControllerView:
    @staticmethod
    def user_choice():
        while True:
            print('\n1. Add a player')
            print('2. Create a new Tournament ')
            print('3. Launch a Tournament')
            print('4. Retrieve all Players in Data Base')
            print('5. Retrieve all Tournaments in Data Base')
            print('6. Quit')
            input_choice_value = int(input('Make your choice: '))
            if (input_choice_value == 1
                    or input_choice_value == 2
                    or input_choice_value == 3
                    or input_choice_value == 4
                    or input_choice_value == 5
                    or input_choice_value == 6):
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')

    @staticmethod
    def choose_tournament():
        return int(input('\nSelect a tournament by is ID : '))