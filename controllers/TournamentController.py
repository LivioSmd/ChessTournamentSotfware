from models.PlayerModel import PlayerModel
from models.RoundModel import RoundModel
from models.MatchModel import MatchModel
from views.TournamentControllerView import TournamentControllerView
import random
import datetime


class TournamentController:
    def MainMethod(self, tournament):
        TournamentControllerView.RoundInfo(tournament)
        while True:
            choice = TournamentControllerView.UserChoice()
            if choice == 1:
                if not tournament.all_rounds_list:
                    self.LaunchRound(tournament)
                elif "Undefined" in tournament.all_rounds_list[-1]["endDate"]:
                    TournamentControllerView.ImpossibleLaunchRound()
                else:
                    self.LaunchRound(tournament)
            elif choice == 2:
                self.LaunchRound(tournament)
            elif choice == 3:
                self.RetrieveTournamentNameDates(tournament)
            elif choice == 4:
                self.RetrieveTournamentPlayerList(tournament)
            elif choice == 5:
                self.RetrieveTournamentRoundsMatchs(tournament)
            elif choice == 6:
                break

    @staticmethod
    def Rematches(test_rematch, tournament):
        all_rounds = tournament.all_rounds_list
        for round in all_rounds:
            match_list = round['matchList']
            print(f'round matchList: {round['matchList']}')
            for match in match_list:
                p1 = match[0][0]
                p2 = match[1][0]
                every_match = [p1, p2]
                print(f'every_match : {every_match}')
                if every_match == test_rematch:
                    print('HELP')
                    return test_rematch

    def LaunchRound(self, tournament):
        while True:
            if self.TournamentEnded(tournament):
                break

            if tournament.current_round == 1:
                if not tournament.all_rounds_list:
                    self.FirstRound(tournament)
                    break
                else:
                    self.CompleteRound(tournament)
                    break
            else:
                if "Undefined" in tournament.all_rounds_list[-1]["endDate"]:
                    self.CompleteRound(tournament)
                    self.TournamentEnded(tournament)
                    break
                else:
                    self.NextRound(tournament)
                    break

    @staticmethod
    def FirstRound(tournament):
        player_list = tournament.player_list
        round_model = RoundModel()
        now = datetime.datetime.now()
        date_formatted = now.strftime("%Y-%m-%d %H:%M:%S")

        random.shuffle(player_list)

        for i in range(0, len(player_list), 2):
            if i < len(player_list) - 1:
                player_1 = PlayerModel().player_retrieval(player_list[i].id)
                player_2 = PlayerModel().player_retrieval(player_list[i + 1].id)
                new_match = MatchModel(player_1.id, 0, player_2.id, 0).Match()
                round_model.match_list.append(new_match)

        round_model.name = f'Round {tournament.current_round}'
        round_model.start_date = date_formatted
        TournamentControllerView.RoundName(tournament)

        match_list = round_model.match_list

        for i in range(len(match_list)):
            player_1 = PlayerModel().player_retrieval(match_list[i][0][0]).name
            player_2 = PlayerModel().player_retrieval(match_list[i][1][0]).name
            TournamentControllerView.MatchList(player_1, player_2)

        tournament.all_rounds_list.append(round_model.serialize())
        tournament.update()

    def NextRound(self, tournament):
        now = datetime.datetime.now()
        date_formatted = now.strftime("%Y-%m-%d %H:%M:%S")
        all_rounds_list = tournament.all_rounds_list
        round_model = RoundModel()

        last_round_player_list = all_rounds_list[-1]['matchList']

        sorted_players = TournamentControllerView.DisplayScoreList(last_round_player_list)

        TournamentControllerView.RoundName(tournament)

        skip_next = False
        for i in range(0, len(sorted_players), 2):
            if skip_next:
                skip_next = False
                continue

            if i < len(sorted_players) - 1:
                print(f'sorted_players: {sorted_players}')
                p1 = sorted_players[i][0]
                p2 = sorted_players[i + 1][0]

                player_1 = PlayerModel().player_retrieval(p1)
                player_1_score = sorted_players[i][1]
                player_2 = PlayerModel().player_retrieval(p2)
                player_2_score = sorted_players[i + 1][1]
                print(p1, p2)

                new_match_test = [p1, p2]
                test_rematch = self.Rematches(new_match_test, tournament)
                if test_rematch == new_match_test:
                    next_player_1 = PlayerModel().player_retrieval(sorted_players[i + 2][0])
                    next_player_1_score = sorted_players[i + 2][1]
                    next_player_2 = PlayerModel().player_retrieval(sorted_players[i + 3][0])
                    next_player_2_score = sorted_players[i + 3][1]

                    new_match = MatchModel(player_1.id, player_1_score, next_player_1.id, next_player_1_score).Match()
                    new_match_2 = MatchModel(player_2.id, player_2_score, next_player_2.id, next_player_2_score).Match()
                    round_model.match_list.append(new_match)
                    round_model.match_list.append(new_match_2)
                    TournamentControllerView.MatchList(player_1.name, next_player_1.name)
                    TournamentControllerView.MatchList(player_2.name, next_player_2.name)
                    skip_next = True
                else:
                    new_match = MatchModel(player_1.id, player_1_score, player_2.id, player_2_score).Match()
                    round_model.match_list.append(new_match)
                    TournamentControllerView.MatchList(player_1.name, player_2.name)
        print(round_model.match_list)
        round_model.name = f'Round {tournament.current_round}'
        round_model.start_date = date_formatted

        tournament.all_rounds_list.append(round_model.serialize())
        print(tournament.all_rounds_list)
        tournament.update()

    @staticmethod
    def CompleteRound(tournament):
        now = datetime.datetime.now()
        date_formatted = now.strftime("%Y-%m-%d %H:%M:%S")

        last_round_model = tournament.all_rounds_list[-1]
        match_list = last_round_model['matchList']
        new_round_model = RoundModel()

        print(last_round_model)
        print(match_list)

        for i in range(len(match_list)):
            player_1 = PlayerModel().player_retrieval(match_list[i][0][0])
            player_1_score = match_list[i][0][1]
            player_2 = PlayerModel().player_retrieval(match_list[i][1][0])
            player_2_score = match_list[i][1][1]

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
        new_round_model.start_date = last_round_model["startDate"]
        new_round_model.end_date = date_formatted

        print(new_round_model)
        print(new_round_model.match_list)

        tournament.all_rounds_list[-1] = new_round_model.serialize()
        tournament.current_round += 1
        tournament.update()

    @staticmethod
    def RetrieveTournamentNameDates(tournament):
        TournamentControllerView().DisplayNameDates(tournament)

    @staticmethod
    def RetrieveTournamentPlayerList(tournament):
        TournamentControllerView().DisplayPlayerList(tournament)

    @staticmethod
    def RetrieveTournamentRoundsMatchs(tournament):
        for round in tournament.all_rounds_list:
            the_round = RoundModel().deserialize(round)
            match_list = the_round.match_list
            TournamentControllerView().DisplayRounds(the_round)
            for match in match_list:
                player_1 = PlayerModel().player_retrieval(match[0][0]).name
                player_1_score = match[0][1]
                player_2 = PlayerModel().player_retrieval(match[1][0]).name
                player_2_score = match[1][1]
                TournamentControllerView().DisplayMatches(player_1, player_1_score, player_2, player_2_score)

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

    #   TODO découper les infos du rapport du tournoi = ok
    #   TODO relire le cahier des charges et verif = ok
    #   TODO lire la grille d'éval (discord)
