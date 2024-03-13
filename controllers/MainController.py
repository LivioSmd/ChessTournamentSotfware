from views.PlayerView import PlayerView
from views.Utils import Utils
from models.PlayerModel import PlayerModel
from models.PlayerModel import ManagePlayer
from views.TournamentView import TournamentView


class MainController:

    def MainMethod(self):
        while True:
            choice = PlayerView.UserChoice()
            if choice == 1:
                self.RegisterPlayer()
            elif choice == 2:
                MainController.DisplayPlayersInDataBase()
            elif choice == 3:
                Utils.CloseProgram()
                break
            elif choice == 4:
                MainController.SetTournament()

    def RegisterPlayer(self):
        player_info = PlayerView.RetrievePlayerInfo()
        new_player = PlayerModel(player_info['Name'], player_info['Surname'], player_info['BirthDate'])
        ManagePlayer.insert_player_in_db(ManagePlayer(new_player).serialize())

    @staticmethod
    def DisplayPlayersInDataBase():
        PlayerView.DisplayDataBase(ManagePlayer.deserialize(ManagePlayer.retrieve_all_players_from_db()))

    @staticmethod
    def SetTournament():
        TournamentView.SetTournamentName()
        TournamentView.SetTournamentPlace()
        TournamentView.SetTournamentStartDate()
        TournamentView.SetTournamentEndDate()
        TournamentView.SetTournamentRound()
        TournamentView.SetTournamentDescription()
        TournamentView.ChooseTournamentPlayers(ManagePlayer.deserialize(ManagePlayer.retrieve_all_players_from_db()))

    """""
    @staticmethod
    def ChooseTournamentPlayers():
        choice_list = []

        Utils.DbListPlayersMessage()

        TournamentView.ChooseTournamentPlayers(ManagePlayer.deserialize(ManagePlayer.retrieve_all_players_from_db()))
    """""


MainController().MainMethod()  # main.py pour lancer
