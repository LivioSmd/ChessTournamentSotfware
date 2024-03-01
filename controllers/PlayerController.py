from views.MainView import MainView
from models.MainModel import CreatePlayer
from tinydb import TinyDB

db = TinyDB('../datas/data.json')


class Main:
    def start(self):
        while True:
            choice = MainView.UserChoice()
            if choice == 1:
                player = CreatePlayer().RetrievePlayer(MainView)
                MainView.RecapPlayerRegistered(player)
                db.insert({'Name': player["Name"], 'Surname': player["Surname"], 'Birth date': player["Birth Date"]})
                MainView.RetrieveAllPlayerInDataBase()
            elif choice == 2:
                MainView.EndProgram()
                break
            elif choice == 3:
                MainView.RetrieveAllPlayerInDataBase()
                break


Main().start()
