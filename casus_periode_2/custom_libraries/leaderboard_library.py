from custom_libraries import menu_library
from custom_libraries import database_accessing_library


class Leaderboard:

    leaderboard = []

    def __init__(self):
        self.output_menu_instance = menu_library.OutputMenus()
        self.user_dictionary = database_accessing_library.Dal.load_a_file('user_database')

    @staticmethod
    def making_score_list(user_dict_given):
        user_list = []
        for name in user_dict_given['users']:
            user_list.append(user_dict_given['users'][name]['score'])
        return user_list

    @staticmethod
    def score_board(user_list):
        new_user_list = sorted(user_list, reverse=True)
        return new_user_list

    def main_leaderboard(self):
        user_dictionary = self.user_dictionary
        user_list = self.making_score_list(user_dictionary)
        score_list = self.score_board(user_list)
        leaderboard = self.user_insert(score_list)
        self.output_menu_instance.leaderboard_output(score_list, leaderboard)

    def user_insert(self, user_list):
        length = len(user_list)
        n = 0
        user_list_rank = []
        while length > n:
            for name in self.user_dictionary['users']:
                if self.user_dictionary['users'][name]['score'] == user_list[n]:
                    user_list_rank.append(name)

            n += 1
        return user_list_rank

    def reset_leaderboard(self):
        base_user_database = self.user_dictionary['users']
        for var in base_user_database.keys():
            base_user_database[var]['score'] = 0
        database_accessing_library.Dal.save_a_file('user-database', base_user_database)
