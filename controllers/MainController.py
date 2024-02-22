from views.MainView import MainView


class Main:

    def start(self):
        while True:
            choice = MainView.UserChoice()
            if choice == 1:
                player = CreatePlayer().RetrievePlayer()
                MainView.RecapPlayerRegistered(player)
            elif choice == 2:
                MainView.EndProgram()
                break


class CreatePlayer:

    def RetrievePlayer(self):
        return {
            "Name": MainView.RetrieveName(),
            "Surname": MainView.RetrieveSurname(),
            "Birth Date": MainView.RetrieveBirthDate(),
        }


Main().start()
