import re


class TournamentView:

    @staticmethod
    def SetTournamentName():
        while True:
            input_tournament_name = input('\nEnter the tournament Name: ').strip()
            if input_tournament_name.isdigit():
                print(f'"{input_tournament_name}" is not a valid name.')
            else:
                return input_tournament_name

    @staticmethod
    def SetTournamentPlace():
        input_tournament_place = input('Enter the tournament Place: ')
        return input_tournament_place

    @staticmethod
    def SetTournamentStartDate():
        while True:
            input_tournament_start_date = input('Enter the tournament Start Date (DD/MM/YYYY): ').strip()
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', input_tournament_start_date):
                print(f'"{input_tournament_start_date}" is not a valid Date.')
            else:
                return input_tournament_start_date

    @staticmethod
    def SetTournamentEndDate():
        while True:
            input_tournament_end_date = input('Enter the tournament End Date (DD/MM/YYYY): ').strip()
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', input_tournament_end_date):
                print(f'"{input_tournament_end_date}" is not a valid Date.')
            else:
                return input_tournament_end_date

    @staticmethod
    def SetTournamentRound():
        while True:
            input_tournament_ask_round = input('The number of Rounds is set to 4 by default, '
                                               'do you want to change it? (y/n)').strip()
            if input_tournament_ask_round.lower() == 'y':
                input_tournament_round = input('Enter number of Rounds: ')
                if input_tournament_round.isdigit():
                    return int(input_tournament_round)
                else:
                    print(f'"{input_tournament_round}" is not a number.')
            elif input_tournament_ask_round.lower() == 'n':
                return 4
            else:
                print(f'"{input_tournament_ask_round}" is not one of the choices.')

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
                choice_list.append(player)
                players_in_db.remove(player)
        while True:
            for player in players_in_db:
                print(f'{player}')
            if len(choice_list) >= 2:  # TODO add 8
                input_choose_players_extra = input('Another player (enter "N" to stop) ?: ').strip()
                if input_choose_players_extra.lower() == 'n':
                    break
                else:
                    for player in players_in_db:
                        if player.id == int(input_choose_players_extra):
                            choice_list.append(player)
                            players_in_db.remove(player)
            else:
                input_choose_players = int(input(f'Another player ({len(choice_list)}/2): ').strip())  # TODO add 8
                for player in players_in_db:
                    if player.id == input_choose_players:
                        choice_list.append(player)
                        players_in_db.remove(player)
        return choice_list

    @staticmethod
    def DisplayDataBase(data):
        for tournament in data:
            print(f'{tournament}')