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
            print(f'{index}. {player}')

        input_choose_first_player = int(input("Select the players for your tournament one "
                                              "by one using their number:").strip())
        choice_first_player = players_in_db[input_choose_first_player]
        choice_list.append(choice_first_player)
        players_in_db.remove(choice_first_player)
        while True:
            for index, player in enumerate(players_in_db):
                print(f'{index}. {player}')
            if len(choice_list) >= 2:  # TODO add 8
                input_choose_players_extra = input('Another player ("N" to stop | "D" to display selected '
                                                   'players) ?: ').strip()
                if input_choose_players_extra.lower() == 'n':
                    break
                elif input_choose_players_extra.lower() == 'd':
                    print(f' Selected players : {choice_list} \n -------------')
                else:
                    extra_player_choice = players_in_db[int(input_choose_players_extra)]
                    choice_list.append(extra_player_choice)
                    players_in_db.remove(extra_player_choice)
            else:
                input_choose_players = int(input(f'Another player ({len(choice_list)}/2): ').strip())
                choice_player = players_in_db[input_choose_players]
                choice_list.append(choice_player)
                players_in_db.remove(choice_player)
        print(f'Selected players : {choice_list}')
        return choice_list

    @staticmethod
    def SetTournamentDescription():
        input_tournament_description = input('Enter the tournament Description: ')
        return input_tournament_description
