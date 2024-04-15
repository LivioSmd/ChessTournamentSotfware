from views.PlayerView import PlayerView
from views.Utils import Utils
from views.TournamentView import TournamentView
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from models.RoundModel import RoundModel
from models.MatchModel import MatchModel
import random


class MainController:

    def MainMethod(self):
        while True:
            choice = PlayerView.UserChoice()
            if choice == 1:
                self.LaunchTournament()
            elif choice == 2:
                self.DisplayPlayersInDataBase()
            elif choice == 3:
                Utils.CloseProgram()
                break
            elif choice == 4:
                self.SetTournament()

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
        Utils.SuccessTournament(tournament.name, tournament.start_date, tournament.end_date)

    @staticmethod   # TODO faire un autre controller
    def LaunchTournament():
        tournament = TournamentModel().tournament_retrieval(11)
        tournament.all_rounds_list = RoundModel()
        player_list = tournament.player_list
        print(f'Classic list : {player_list}')
        random.shuffle(player_list)
        print(f'Random list : {player_list}')
        player_size = len(player_list)

        for i in range(0, player_size, 2):
            if i < player_size - 1:
                instance = MatchModel(PlayerModel.player_retrieval(PlayerModel(), player_list[i]).name,
                                      PlayerModel.player_retrieval(PlayerModel(), player_list[i + 1]).name).match()
                tournament.all_rounds_list.match_list.append(instance)
        print(tournament)

        print("----------- Round 1 -----------")

        for i in range(len(tournament.all_rounds_list.match_list)):
            print(f'        {tournament.all_rounds_list.match_list[i][0][0]} vs {tournament.all_rounds_list.match_list[i][1][0]}')


MainController().MainMethod()  # main.py pour lancer
