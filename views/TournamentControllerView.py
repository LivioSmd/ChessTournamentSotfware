class TournamentControllerView:

    @staticmethod
    def user_choice():
        while True:
            print('\n1. Launch or Continue a Round')
            print('2. Stop a Round')
            print("3. Retrieve tournament information's")
            print("4. Retrieve tournament player list")
            print("5. Retrieve information on tournament rounds and matches")
            print('6. Back to main menu')
            input_choice_value = int(input('Make your choice: '))
            if (input_choice_value == 1
                    or input_choice_value == 2
                    or input_choice_value == 3
                    or input_choice_value == 4
                    or input_choice_value == 5
                    or input_choice_value == 6):
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')

    @staticmethod
    def round_name(tournament):
        print(f'\n--- ROUND {tournament.current_round} ---')

    @staticmethod
    def match_list(player_1, player_2):
        print(f'{player_1} VS {player_2}')

    @staticmethod
    def scoring(player_1, player_2):
        print(f'\nMatch : (1) {player_1.name} VS (2) {player_2.name}')
        return input('who won ? Enter "1" for player 1, "2" for player 2, "3" for draw: ')

    @staticmethod
    def not_found(choice):
        print(f'No tournament matches id = "{choice}"')

    @staticmethod
    def round_info(tournament):
        print(
            f'\nFor this Tournament current Round is Actually '
            f'[{tournament.current_round - 1}/{tournament.round_total}]')

    @staticmethod
    def round_over():
        return input('\nIs the round over (y/n) ?: ')

    @staticmethod
    def new_score(player):
        return int(input(f'\nEnter {player.name} new score: '))

    @staticmethod
    def display_score_list(match_list):
        players_list = []
        for i in range(len(match_list)):
            player_1 = match_list[i][0]
            player_2 = match_list[i][1]
            players_list.append(player_1)
            players_list.append(player_2)

        sorted_players = sorted(players_list, key=lambda pl: pl[1], reverse=True)
        return sorted_players

    @staticmethod
    def display_tournament_players(data):
        sorted_players = sorted(data, key=lambda p: p.name)
        for player in sorted_players:
            print(f'        - {player}')

    @staticmethod
    def display_name_dates(tournament):
        print(f'\n- Tournament Name: {tournament.name}')
        print(f'- Tournament Start Date: {tournament.start_date}')
        print(f'- Tournament End Date: {tournament.end_date}')

    def display_player_list(self, tournament):
        print('- Tournament Players List:')
        self.display_tournament_players(tournament.player_list)

    @staticmethod
    def display_rounds(the_round):
        print(f'        - {the_round}')

    @staticmethod
    def display_matches(player_1, player_1_score, player_2, player_2_score):
        print(f'                - {player_1} ({player_1_score})    VS    {player_2} ({player_2_score})')

    @staticmethod
    def impossible_launch_round():
        print('\nImpossible to launch a round, because a round is already in progress ')

    @staticmethod
    def tournament_end():
        print('\n --- END OF THE TOURNAMENT ---')

    @staticmethod
    def display_end_list(players_list):
        sorted_players = sorted(players_list, key=lambda pl: pl[1], reverse=True)
        return sorted_players

    @staticmethod
    def tournament_end_list(index, player):
        print(f'{index + 1}. {player[0].name.ljust(15)}Score : {player[1]} pts')
        # "ljust(15)" aligns the player's name on the left with a width of 15 characters
