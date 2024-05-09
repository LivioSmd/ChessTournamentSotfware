from views.PlayerView import PlayerView
from views.Utils import Utils
from views.TournamentView import TournamentView
from views.MainControllerView import MainControllerView
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from controllers.TournamentController import TournamentController


class MainController:
    def main_method(self):
        while True:
            choice = MainControllerView.user_choice()
            if choice == 1:
                self.register_player()
            elif choice == 2:
                self.set_tournament()
            elif choice == 3:
                TournamentController().main_method(self.choose_tournament())
            elif choice == 4:
                self.display_players_in_data_base()
            elif choice == 5:
                self.display_tournaments_in_data_base()
            elif choice == 6:
                Utils.close_program()
                break

    @staticmethod
    def register_player():
        player_info = PlayerView().retrieve_player_info()
        new_player = PlayerModel(player_info['name'], player_info['surname'], player_info['birthDate'])
        PlayerModel.insert_player_in_db(new_player)

    def choose_tournament(self):
        self.display_tournaments_in_data_base()
        tournament_id = MainControllerView.choose_tournament()
        return TournamentModel().tournament_retrieval(tournament_id)

    @staticmethod
    def display_players_in_data_base():
        Utils.db_list_players_message()
        PlayerView.display_data_base(PlayerModel.retrieve_all_players_from_db())

    @staticmethod
    def display_tournaments_in_data_base():
        Utils.db_list_tournaments_message()
        TournamentView.display_data_base(TournamentModel.retrieve_all_tournaments_from_db())

    @staticmethod
    def set_tournament():
        tournament = TournamentModel(
            TournamentView.set_tournament_name(),
            TournamentView.set_tournament_place(),
            TournamentView.set_tournament_start_date(),
            TournamentView.set_tournament_end_date(),
            TournamentView.set_tournament_round(),
            TournamentView.set_tournament_description(),
            TournamentView.choose_tournament_players(PlayerModel.retrieve_all_players_from_db())
        )
        TournamentModel.insert_tournament_in_db(tournament)
        Utils.success_tournament(tournament.name, tournament.start_date, tournament.end_date, tournament.id)
        TournamentController().main_method(tournament)


MainController().main_method()  # main.py pour lancer
