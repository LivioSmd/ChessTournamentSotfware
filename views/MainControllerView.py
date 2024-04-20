
class MainControllerView:
    @staticmethod
    def UserChoice():
        while True:
            print('\n1. Add a player')
            print('2. Create a new Tournament ')
            print('3. Launch a Tournament')
            print('4. Retrieve all players in Data Base')
            print('5. Quit')
            input_choice_value = int(input('Make your choice: '))
            if (input_choice_value == 1
                    or input_choice_value == 2
                    or input_choice_value == 3
                    or input_choice_value == 4
                    or input_choice_value == 5):
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')