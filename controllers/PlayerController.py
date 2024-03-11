from views.PlayerView import PlayerView
from views.Utils import Utils
from models.PlayerModel import PlayerModel
from models.PlayerModel import ManagePlayer
from models.MatchModel import MatchModel


class PlayerController:     # TODO rename
    @staticmethod
    def CreatePlayer():     # TODO rename
        while True:
            choice = PlayerView.UserChoice()
            if choice == 1:     # TODO faire des methodes pour les choix
                player_infos = PlayerView.RetrievePlayerInfo()
                new_player = PlayerModel(player_infos['Name'], player_infos['Surname'], player_infos['BirthDate'])
                if ManagePlayer(new_player).serialize():
                    Utils.DataBaseSuccess()
            elif choice == 2:
                Utils.CloseProgram()
                break
            elif choice == 3:


                """""
                def is_even_number(number):
                    return number % 2 == 0

                player_a_info = ""
                player_b_info = ""

                for index, player in enumerate(ManagePlayer.deserialize()):
                    if is_even_number(index):
                        player_a = ManagePlayer.deserialize()[index]
                        player_a_info = player_a["Name"] + " " + player_a["Surname"]
                    else:
                        player_b = ManagePlayer.deserialize()[index]
                        player_b_info = player_b["Name"] + " " + player_b["Surname"]

                print(MatchModel(player_a_info, player_b_info).match())
                break
                """""


PlayerController().CreatePlayer()
