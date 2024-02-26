
class CreatePlayer:
    def RetrievePlayer(self, MainView):
        return {
            "Name": MainView.RetrieveName(),
            "Surname": MainView.RetrieveSurname(),
            "Birth Date": MainView.RetrieveBirthDate(),
        }