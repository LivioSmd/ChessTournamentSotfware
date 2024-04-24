from models.PlayerModel import PlayerModel
from models.RoundModel import RoundModel
from models.MatchModel import MatchModel
from views.TournamentControllerView import TournamentControllerView
import random
from tinydb import TinyDB

db = TinyDB('../datas/data.json')
tournaments_table = db.table('tournaments')


class TournamentController:
    def MainMethod(self, tournament):  # Lancer un round, arreter un round
        TournamentControllerView.RoundInfo(tournament)
        while True:
            choice = TournamentControllerView.UserChoice()
            if choice == 1:
                self.LaunchRound(tournament)
            elif choice == 2 or choice == 3:
                break

    def LaunchRound(self, tournament):
        while True:
            if self.TournamentEnded(tournament):
                break

            if tournament.current_round == 1:
                self.FirstRound(tournament)
                break
            else:
                self.NextRound(tournament)
                self.TournamentEnded(tournament)
                break


    @staticmethod
    def FirstRound(tournament):
        player_list = tournament.player_list
        round_model = RoundModel()
        new_round_model = RoundModel()

        round_date = TournamentControllerView.RoundDate()
        round_start_date = round_date[0]
        round_end_date = round_date[1]

        random.shuffle(player_list)

        for i in range(0, len(player_list), 2):
            if i < len(player_list) - 1:
                player_1 = PlayerModel().player_retrieval(player_list[i].id)
                player_2 = PlayerModel().player_retrieval(player_list[i + 1].id)
                new_match = MatchModel(player_1.id, 0, player_2.id, 0).Match()
                round_model.match_list.append(new_match)

        round_model.name = f'Round {tournament.current_round}'
        TournamentControllerView.RoundName(tournament, round_start_date, round_end_date)

        player_list = round_model.match_list

        for i in range(len(player_list)):
            player_1 = PlayerModel().player_retrieval(player_list[i][0][0]).name
            player_2 = PlayerModel().player_retrieval(player_list[i][1][0]).name
            TournamentControllerView.MatchList(player_1, player_2)

        round_over = TournamentControllerView.RoundOver()

        if round_over.lower() == "y":
            for i in range(len(player_list)):
                player_1 = PlayerModel().player_retrieval(player_list[i][0][0])
                player_1_score = player_list[i][0][1]
                player_2 = PlayerModel().player_retrieval(player_list[i][1][0])
                player_2_score = player_list[i][1][1]

                score = TournamentControllerView.Scoring(player_1, player_2)

                if int(score) == 1:
                    player_1_score += 1
                elif int(score) == 2:
                    player_2_score += 1
                elif int(score) == 3:
                    player_1_score += 0.5
                    player_2_score += 0.5

                new_match = MatchModel(player_1.id, player_1_score, player_2.id, player_2_score).Match()
                new_round_model.match_list.append(new_match)

            new_round_model.name = f'Round {tournament.current_round}'
            new_round_model.start_date = round_start_date
            new_round_model.end_date = round_end_date

            tournament.all_rounds_list.append(new_round_model.serialize())
            tournament.current_round += 1
            tournament.update()

    @staticmethod
    def NextRound(tournament):
        all_rounds_list_2 = tournament.all_rounds_list
        new_round_model = RoundModel()

        round_date = TournamentControllerView.RoundDate()
        round_start_date = round_date[0]
        round_end_date = round_date[1]

        last_round_player_list = all_rounds_list_2[-1]['matchList']

        sorted_players = TournamentControllerView.DisplayScoreList(last_round_player_list)

        TournamentControllerView.RoundName(tournament, round_start_date, round_end_date)
        for i in range(0, len(sorted_players), 2):
            if i < len(sorted_players) - 1:
                player_1 = PlayerModel().player_retrieval(sorted_players[i][0]).name
                player_2 = PlayerModel().player_retrieval(sorted_players[i + 1][0]).name
                TournamentControllerView.MatchList(player_1, player_2)
        round_over = TournamentControllerView.RoundOver()

        if round_over.lower() == "y":
            for i in range(0, len(sorted_players), 2):
                if i < len(sorted_players) - 1:
                    player_1 = PlayerModel().player_retrieval(sorted_players[i][0])
                    player_1_score = sorted_players[i][1]
                    player_2 = PlayerModel().player_retrieval(sorted_players[i + 1][0])
                    player_2_score = sorted_players[i][1]
                    score = TournamentControllerView.Scoring(player_1, player_2)

                    if int(score) == 1:
                        player_1_score += 1
                    elif int(score) == 2:
                        player_2_score += 1
                    elif int(score) == 3:
                        player_1_score += 0.5
                        player_2_score += 0.5

                    new_round_list = MatchModel(player_1.id, player_1_score, player_2.id, player_2_score).Match()
                    new_round_model.match_list.append(new_round_list)

            new_round_model.name = f'Round {tournament.current_round}'
            new_round_model.start_date = round_start_date
            new_round_model.end_date = round_end_date

            tournament.all_rounds_list.append(new_round_model.serialize())
            tournament.current_round += 1
            tournament.update()

    @staticmethod
    def TournamentEnded(tournament):
        if tournament.current_round > tournament.round_total:
            TournamentControllerView.TournamentEnd()

            players_list = []
            if int(tournament.current_round) == int(tournament.round_total + 1):
                last_round = tournament.all_rounds_list[-1]['matchList']
                for i in range(len(last_round)):
                    player_1 = [PlayerModel().player_retrieval(last_round[i][0][0]), last_round[i][0][1]]
                    player_2 = [PlayerModel().player_retrieval(last_round[i][1][0]), last_round[i][1][1]]
                    players_list.append(player_1)
                    players_list.append(player_2)

                sorted_players = TournamentControllerView.DisplayEndList(players_list)
                for index, player in enumerate(sorted_players):
                    TournamentControllerView.TournamentEndList(index, player)

                return True

    #   TODO attribuer les dates des rounds automatiquement
    #   TODO stopper les tournois a la place du round est finis (pour par exemple lancer plusieurs tournoi)
    #   TODO faire que les joueurs ne retombent pas les uns contre les autres
    #   TODO faire les rapports

