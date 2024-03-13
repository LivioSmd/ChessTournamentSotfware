class TournamentView:

    @staticmethod
    def SetTournamentName():
        input_tournament_name = input('Enter the tournament Name: ')
        return input_tournament_name

    @staticmethod
    def SetTournamentPlace():
        input_tournament_place = input('Enter the tournament Place: ')
        return input_tournament_place

    @staticmethod
    def SetTournamentStartDate():
        input_tournament_start_date = input('Enter the tournament Start date (DD/MM/YYYY): ')
        return input_tournament_start_date

    @staticmethod
    def SetTournamentEndDate():
        input_tournament_end_date = input('Enter the tournament End date (DD/MM/YYYY): ')
        return input_tournament_end_date

    @staticmethod
    def SetTournamentRound():
        input_tournament_ask_round = input('The number of Rounds is set to 4 by default, '
                                           'do you want to change it? (y/n)').strip()
        if input_tournament_ask_round.lower() == 'y':
            input_tournament_end_date = input('Enter number of Rounds: ')
            print(input_tournament_end_date)
            return input_tournament_end_date
        elif input_tournament_ask_round.lower() == 'n':
            return 4

    @staticmethod
    def ChooseTournamentPlayers(players_in_db):
        choice_list = []

        print("Here's a list of all the players in the database.")

        for index, player in enumerate(players_in_db):
            player = players_in_db.get(index)
            print(f'{index}. {player['Name']} {player['Surname']}')


        input_choose_first_player = input("Select the players for your tournament one "
                                          "by one using their number (1) :").strip()
        choice_list.append(input_choose_first_player)  # stocker les instances de joueurs
        while True:
            input_choose_players = input("Another player (N to stop) ?: ").strip()
            if input_choose_players.lower() == 'n':
                break
            choice_list.append(input_choose_players)
        print(choice_list)
        return choice_list  # minimum 8 joueurs

    @staticmethod
    def SetTournamentDescription():
        input_tournament_description = input('Enter the tournament Description: ')
        return input_tournament_description
