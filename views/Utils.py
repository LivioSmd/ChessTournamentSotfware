class Utils:

    @staticmethod
    def CloseProgram():
        return print('---- Program out ----')

    @staticmethod
    def DbListPlayersMessage():
        return print("\n---- Here's a list of all the players in the database  ----")

    @staticmethod
    def SuccessTournament(name, start, end):
        print(f"\n---- New Tournament Registered: {name},  from: {start} to: {end} ! ----\n")
