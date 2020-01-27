from custom_libraries import menu_library
from custom_libraries import database_accessing_library

class Developer:
    print('hi')
    # def __init__(self):
    #     self.output_instance = menu_library.OutputMenus()
    #     self.database_accessing_instance = database_accessing_library.Dal()
    #
    # def developer_console(self):
    #
    #     developer_flag = True
    #     while developer_flag:
    #         self.output_menu_instance.developer_options()
    #         developer_choice = input('... ')
    #         print('-' * 50)
    #         if developer_choice.lower() == 'reset-users':
    #             self.reset_users()
    #         elif developer_choice.lower() == 'reset-questions':
    #             self.reset_questions()
    #         elif developer_choice.lower() == 'add-question':
    #             self.add_question()
    #         elif developer_choice.lower() == 'nuke':
    #             confirmation = input('are you sure? ')
    #             if confirmation.lower() == 'yes':
    #                 self.nuke()
    #             elif confirmation.lower() == 'q':
    #                 self.output_menu_instance.quit()
    #                 developer_flag = False
    #         elif developer_choice.lower() == 'reset-leaderboard':
    #             self.reset_leaderboard()
    #         elif developer_choice.lower() == 'q':
    #             developer_flag = False
    #             self.output_menu_instance.quit()
    #
    #         elif developer_choice.lower() == 'main':
    #             developer_flag = False
    #             self.back_to_main_menu()
    #
    # def reset_users(self):
    #
    #     self.database_accessing_instance.save_a_file('user_database', database_accessing_library.user_database_backup)
    #
    # def reset_questions(self):
    #
    #     self.database_accessing_instance.save_a_file('question_database', database_accessing_library.code_database_backup)
    #
    #