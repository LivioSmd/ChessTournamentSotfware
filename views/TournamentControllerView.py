class TournamentControllerView:

    @staticmethod
    def UserChoice():
        while True:
            input_choice_value = input('\nEnter tournament id (Press Q to Quit): ')
            if input_choice_value.lower() == 'q' or input_choice_value.isdigit():
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')

    """
    @staticmethod
    def UserChoice():
        while True:
            input_choice_value = input('\nEnter tournament id (Press Q to Quit): ')
            if input_choice_value.lower() == 'q' or input_choice_value.isdigit():
                return input_choice_value
            else:
                print(f'{input_choice_value} is not one of the choices.\n -------------')
    """

    @staticmethod
    def MatchList(tournament, currentRound):
        print(f'\n--- ROUND {currentRound} ---')

        for i in range(len(tournament.all_rounds_list.match_list)):
            print(
                f'{tournament.all_rounds_list.match_list[i][0][0]} VS {tournament.all_rounds_list.match_list[i][1][0]}')

    @staticmethod
    def NotFound(choice):
        print(f'No tournament matches id = "{choice}"')

    @staticmethod
    def RoundOver():
        return input('\nIs the round over (y/n) ?: ')

    @staticmethod
    def NewScore(player):
        return int(input(f'\nEnter {player.name} new score: '))

    @staticmethod
    def DisplayScoreList(players_list, currentRound):  # TODO add 'Round + num du round'
        print(f'\n--- SCORE LIST ROUND {currentRound} ---')
        sorted_list = sorted(players_list, key=lambda p: p.score,
                             reverse=True)  # Trie décroissant sur les scores  des joueurs

        for player in sorted_list:
            print(f'- {player.name} [{player.score}]')

        return sorted_list

    @staticmethod
    def TournamentEnd(players_list):
        print('\n --- END OF THE TOURNAMENT ---')
        print('--- Top 3 ---')
        for index, player in enumerate(players_list[:3]):
            print(f"[{index + 1}] {player.name} -> {player.score}")
