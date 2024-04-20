from views.PlayerView import PlayerView
from views.Utils import Utils
from views.TournamentView import TournamentView
from views.MainControllerView import MainControllerView
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from controllers.TournamentController import TournamentControllers


class MainController:

    def MainMethod(self):
        while True:
            choice = MainControllerView.UserChoice()
            if choice == 1:
                self.RegisterPlayer()
            elif choice == 2:
                self.SetTournament()
            elif choice == 3:
                TournamentControllers().MainMethod()
            elif choice == 4:
                self.DisplayPlayersInDataBase()
            elif choice == 5:
                Utils.CloseProgram()
                break

    @staticmethod
    def RegisterPlayer():
        player_info = PlayerView().RetrievePlayerInfo()
        new_player = PlayerModel(player_info['name'], player_info['surname'], player_info['birthDate'])
        PlayerModel.insert_player_in_db(new_player)

    @staticmethod
    def DisplayPlayersInDataBase():
        Utils.DbListPlayersMessage()
        PlayerView.DisplayDataBase(PlayerModel.retrieve_all_players_from_db())

    @staticmethod
    def SetTournament():
        tournament = TournamentModel(
            TournamentView.SetTournamentName(),
            TournamentView.SetTournamentPlace(),
            TournamentView.SetTournamentStartDate(),
            TournamentView.SetTournamentEndDate(),
            TournamentView.SetTournamentRound(),
            TournamentView.SetTournamentDescription(),
            TournamentView.ChooseTournamentPlayers(PlayerModel.retrieve_all_players_from_db())
        )
        TournamentModel.insert_tournament_in_db(tournament)
        Utils.SuccessTournament(tournament.name, tournament.start_date, tournament.end_date, tournament.id)


MainController().MainMethod()  # main.py pour lancer
