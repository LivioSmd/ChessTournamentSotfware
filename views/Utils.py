class Utils:
    @staticmethod
    def close_program():
        return print('---- Program out ----')

    @staticmethod
    def db_list_players_message():
        return print("\n---- Here's a list of all the players in the database  ----")

    @staticmethod
    def db_list_tournaments_message():
        return print("\n---- Here's a list of all the tournaments in the database  ----")

    @staticmethod
    def success_tournament(name, start, end, id):
        print(f"\n---- New Tournament Registered:  [{id}]. {name},  from: {start} to: {end} ! ----\n")
