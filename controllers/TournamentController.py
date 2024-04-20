from tinydb import TinyDB
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from models.RoundModel import RoundModel
from models.MatchModel import MatchModel
from views.TournamentControllerView import TournamentControllerView
import random

db = TinyDB('../datas/data.json')
tournaments_table = db.table('tournaments')


class TournamentControllers:

    def MainMethod(self):
        while True:
            choice = TournamentControllerView.UserChoice()
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

    def ChooseTournament(self, choice):
        while True:
            if choice.lower() == 'q':
                return 0
            elif choice.isdigit():
                for tournament in tournaments_table:
                    if int(choice) == int(tournament.doc_id):
                        return self.LaunchTournament(choice)
                else:
                    TournamentControllerView.NotFound(choice)
                    return 0

    @staticmethod
    def LaunchTournament(id):
        tournament = TournamentModel().tournament_retrieval(id)
        player_list = tournament.player_list
        round_model = RoundModel()

        random.shuffle(player_list)

        for i in range(0, len(player_list), 2):
            if i < len(player_list) - 1:
                player_1 = PlayerModel().player_retrieval(player_list[i].id)
                player_2 = PlayerModel().player_retrieval(player_list[i + 1].id)
                new_match = MatchModel(player_1, player_2).match()
                round_model.match_list.append(new_match)

        tournament.all_rounds_list = round_model
        TournamentControllerView.MatchList(tournament, tournament.current_round)
        return tournament

    def Method(self):
        while True:
            choice = TournamentControllerView.UserChoice()
            tournament = self.ChooseTournament(choice)
            new_players_list = []
            sorted_players_list = []
            if tournament == 0:
                break
            else:
                while True:
                    round_over = TournamentControllerView.RoundOver()
                    if round_over.lower() == 'y':
                        player_list = tournament.player_list
                        for player in player_list:
                            new_score = TournamentControllerView.NewScore(player)
                            player.score += new_score
                            new_players_list.append(player)
                        sorted_players_list = TournamentControllerView.DisplayScoreList(new_players_list,
                                                                                        tournament.current_round)
                        tournament.player_list = sorted_players_list
                        tournament.current_round += 1
                        break
                    else:
                        continue
                while True:
                    if int(tournament.current_round) == int(tournament.round_total + 1):
                        TournamentControllerView.TournamentEnd(tournament.player_list)
                        break
                    else:
                        round_model = RoundModel()
                        new_players_list = []

                        for i in range(0, len(sorted_players_list), 2):
                            if i < len(sorted_players_list) - 1:
                                player_1 = sorted_players_list[i]
                                player_2 = sorted_players_list[i + 1]
                                new_match = MatchModel(player_1, player_2).match()
                                round_model.match_list.append(new_match)
                        tournament.all_rounds_list = round_model
                        TournamentControllerView.MatchList(tournament, tournament.current_round)

                        round_over = TournamentControllerView.RoundOver()

                        if round_over.lower() == 'y':
                            player_list = tournament.player_list
                            for player in player_list:
                                new_score = TournamentControllerView.NewScore(player)
                                player.score += new_score
                                new_players_list.append(player)
                            sorted_players_list = TournamentControllerView.DisplayScoreList(new_players_list,
                                                                                            tournament.current_round)
                            tournament.player_list = sorted_players_list
                            tournament.current_round += 1
            break