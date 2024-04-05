class TournamentView:

    @staticmethod
    def SetTournamentName():
        while True:
            input_tournament_name = input('\nEnter the tournament Name: ').strip()
            if input_tournament_name.isdigit():
                print(f'"{input_tournament_name}" is not a valid name.')
            else:
                break  # TODO finir de sécuriser les autres parties du formulaire pour créer un tournoi

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
            return input_tournament_end_date
        elif input_tournament_ask_round.lower() == 'n':
            return 4

    @staticmethod
    def SetTournamentDescription():
        input_tournament_description = input('Enter the tournament Description: ')
        return input_tournament_description

    @staticmethod
    def ChooseTournamentPlayers(players_in_db):
        choice_list = []

        print("Here's a list of all the players in the database.")

        for player in players_in_db:
            print(f'{player}')

        input_choose_first_player = int(input("Select the players for your tournament one "
                                              "by one using their number:").strip())
        for player in players_in_db:
            if player.id == input_choose_first_player:
                choice_list.append(player.id)
                players_in_db.remove(player)
        while True:
            for player in players_in_db:
                print(f'{player}')
            if len(choice_list) >= 2:  # TODO add 8
                input_choose_players_extra = input('Another player ("N" to stop | "D" to display selected '
                                                   'players) ?: ').strip()
                if input_choose_players_extra.lower() == 'n':
                    break
                elif input_choose_players_extra.lower() == 'd':
                    print(f' Selected players : {choice_list} \n -------------')
                else:
                    for player in players_in_db:
                        if player.id == int(input_choose_players_extra):
                            choice_list.append(player.id)
                            players_in_db.remove(player)
            else:
                input_choose_players = int(input(f'Another player ({len(choice_list)}/2): ').strip())
                for player in players_in_db:
                    if player.id == input_choose_players:
                        choice_list.append(player.id)
                        players_in_db.remove(player)
        return choice_list
