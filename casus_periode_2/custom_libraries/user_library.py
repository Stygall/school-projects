from custom_libraries import object_registry_library
from custom_libraries import database_accessing_library
from custom_libraries import quiz_library
from custom_libraries import leaderboard_library
from custom_libraries import menu_library


class User:

    username = ''
    password = ''
    email = ''
    quiz = ''
    score = 0
    codes = []


    # @staticmethod
    # def user_object_to_list(new_user):
    #     user_list = [new_user.email, new_user.password, new_user.quiz]
    #     return user_list

    @staticmethod
    def user_object_to_dictionary(original_user_dictionary, user):
        original_user_dictionary[user['username']] = {'username': user['username'],
                                                   'email': user['email'],
                                                   'password': user['password'],
                                                   'quiz': user['quiz'],
                                                   'score': user['score'],
                                                   'codes': user['codes']}
        print(original_user_dictionary)
        return original_user_dictionary

    @staticmethod
    def edit_account(library):
        print('do you wanna edit your account?'.center(50))
        print('yes / no')
        choice = input().lower()
        if choice in 'yes' or choice =='y':
            print('which of the following do you want to change?'.center(50))
            print('(p)assword')
            print('(e)mail')
            option = input().lower()
            if option == 'e' or option == 'email':
                email_flag = False
                while not email_flag:
                    print('enter your old email'.center(50))
                    old_email = input().lower()
                    if old_email == library['email']:
                        print('give your new email'.center(50))
                        new_email = input().lower()
                        print('verify your new email'.center(50))
                        verify_email = input().lower()
                        if new_email == verify_email:
                            library['email'] = new_email
                            email_flag = True
                        else:
                            print('the email did not match, \n please try again'.center(50))
                    else:
                        print('the email did not match, \n please try again'.center(50))

            elif option == 'p' or option == 'password':
                password_flag = False
                while not password_flag:
                    print('enter your old password'.center(50))
                    old_password = input().lower()
                    if old_password == library['password']:
                        print('give your new password'.center(50))
                        new_password = input().lower()
                        print('verify your new password'.center(50))
                        verify_password = input().lower()
                        if new_password == verify_password:
                            library['password'] = new_password
                            password_flag = True
                        else:
                            print('the email did not match, \n please try again'.center(50))
                    else:
                        print('the email did not match, \n please try again'.center(50))

            elif choice == 'q':
                menu_library.OutputMenus.quit()
        elif choice == 'q':
            menu_library.OutputMenus.quit()
        else:
            print('we will return to the main menu then')

        return library


class Admin:

    username = ''
    password = ''
    email = ''
    rank = ''

    def __init__(self):
        self.database_accessing_library_instance = database_accessing_library.Dal()
        self.object_registry_instance = object_registry_library.Creator()
        self.quiz_instance = quiz_library.Quiz()
        self.leaderboard_instance = leaderboard_library.Leaderboard()
        self.output_menu_instance = menu_library.OutputMenus()
        self.question_instance = quiz_library.Question()

    def admin_console(self, library):

        admin_flag = True
        while admin_flag:
            self.output_menu_instance.admin_console()
            admin_choice = input('... ').lower()
            if admin_choice == 'a':
                admin_flag = False
                print('do you want to change')
                print('a (s)pecific question?')
                print('or')
                print('(a)ll questions?')
                question_choice = input().lower()
                self.object_registry_instance.register_new_question(question_choice, library)
            elif admin_choice == 'r':
                self.leaderboard_instance.reset_leaderboard()
            elif admin_choice == 'e':
                question = self.question_instance.choose_question(library)
                base = self.database_accessing_library_instance.load_a_file('question_database')
                new_base = base[question['code']] = question
                self.database_accessing_library_instance.save_a_file('question_database', new_base)
            elif admin_choice == 'q':
                self.output_menu_instance.quit()
            elif admin_choice == 'main' or admin_choice == 'm':
                menu_library.InputMenus.login()
            else:
                print('invalid input, please try again')



