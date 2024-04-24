class Utils:

    @staticmethod
    def CloseProgram():
        return print('---- Program out ----')

    @staticmethod
    def DbListPlayersMessage():
        return print("\n---- Here's a list of all the players in the database  ----")

    @staticmethod
    def DbListTournamentsMessage():
        return print("\n---- Here's a list of all the tournaments in the database  ----")

    @staticmethod
    def SuccessTournament(name, start, end, id):
        print(f"\n---- New Tournament Registered:  [{id}]. {name},  from: {start} to: {end} ! ----\n")
