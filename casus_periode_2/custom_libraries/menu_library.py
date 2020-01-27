from custom_libraries import object_registry_library
from custom_libraries import database_accessing_library
from custom_libraries import quiz_library
from custom_libraries import user_library
from custom_libraries import leaderboard_library
from custom_libraries import developer_library


class Layout:

    header = '\033[95m'
    ok_blue = '\033[94m'
    ok_green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end_c = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


class OutputMenus:

    def __init__(self):
        self.database_accessing_library_instance = database_accessing_library.Dal()

    @staticmethod
    def startup():

        print()
        print('-' * 50)
        print('welcome to QrUIZ'.center(50))
        print('-' * 50)
        print('enter Q at any time to stop the application'.center(50))
        print('-' * 50)

    @staticmethod
    def welcome_message(username):

        print('-' * 50)
        message = 'welcome ' + username
        print(message.center(50))

    @staticmethod
    def quit():

        print('see you next time!')

    @staticmethod
    def work_in_progress():

        print('-'*50)
        print('this functionality is not fully operational yet,'.center(50))
        print('please try again later'.center(50))
        print('-'*50)

    @staticmethod
    def main_menu():

        print('-' * 50)
        print('choose one of the following options:'.center(50))
        print('(s)can a code'.center(50))
        print('(c)heck the leaderboard'.center(50))
        print('(a)ccount settings'.center(50))
        print('-' * 50)

    @staticmethod
    def ask_question(question):

        print('-' * 50)
        print(question)
        print('-' * 50)

    @staticmethod
    def leaderboard_output(score_list, user_ranking):

        place = 1
        print('-' * 50)
        print('leaderboard:             ')
        print('-' * 50)
        for name in user_ranking:
            print('rank', place, name, 'score', score_list[place - 1])
            place += 1

    @staticmethod
    def wrong_question():

        print('-' * 50)
        print('this code has been scanned before'.center(50))
        print('you can not answer a question twice'.center(50))
        print('please select a different code'.center(50))
        print('-' * 50)

    def print_account(self, library):

        databank = self.database_accessing_library_instance.load_a_file('user_database')
        username = library['username']
        if username in databank['users'].keys():
            print('username:', databank['users'][username]['username'])
            print('password:', databank['users'][username]['password'])
            print('email:', databank['users'][username]['email'])
            print('score:', databank['users'][username]['score'])

    @staticmethod
    def admin_console():

        print('-' * 50)
        print('you have the following options..')
        print('(a)dd a question.')
        print('(e)dit a question.')
        print('(r)eset leaderboard.')
        print('(m)ain menu.')
        print('-' * 50)


class InputMenus:

    def __init__(self):

        self.database_accessing_library_instance = database_accessing_library.Dal()
        self.object_registry_instance = object_registry_library.Creator()
        self.admin_instance = user_library.Admin()
        self.quiz_instance = quiz_library.Quiz()
        self.user_instance = user_library.User()
        self.leaderboard_instance = leaderboard_library.Leaderboard()
        self.output_menu_instance = OutputMenus()
        self.developer_instance = developer_library.Developer()
        self.scanner_instance = database_accessing_library.Scanner()

    def new_user_interface(self):

        reason = 'user_database'
        user_database = self.database_accessing_library_instance.load_a_file(reason)
        original_user_dictionary = user_database['users']
        original_admin_dictionary = user_database['admins']
        new_user = self.object_registry_instance.register_new_user()
        print(new_user)
        new_user_dictionary = self.user_instance.user_object_to_dictionary(original_user_dictionary, new_user)
        new_file = {'users': new_user_dictionary, 'admins': original_admin_dictionary}
        self.database_accessing_library_instance.save_a_file(reason, new_file)
        print('-' * 50)
        print('your account has been successfully registered!'.center(50))
        print('please log in to the application')
        library = self.authentication()
        self.general_user_interface(library)

    @staticmethod
    def login():

        login_flag = True
        choice = ''
        while login_flag:
            print('do you want to login or register?'.center(50))
            choice = input()
            if choice.lower() == 'login' or choice == 'register':
                login_flag = False
            elif choice.lower() == 'q':
                OutputMenus.quit()
                login_flag = False
            else:
                print('invalid input, try again'.center(50))
            print('-' * 50)

        return choice.lower()

    def general_user_interface(self, library):

        # self.output_menu_instance.welcome_message(library)
        general_user_flag = True
        try:
            if library['rank'] == 'admin':
                self.admin_instance.admin_console(library)
        except KeyError:
            while general_user_flag:
                self.output_menu_instance.main_menu()
                choice = input().lower()
                if choice == 'a':
                    self.output_menu_instance.print_account(library)
                    self.user_instance.edit_account(library)
                if choice == 's':
                    scanned_code = self.scanner_instance.scan_a_code(library)
                    new_quiz = self.object_registry_instance.register_new_quiz(scanned_code, library)
                    self.quiz_instance.ask_question(new_quiz)
                elif choice == 'c':
                    self.leaderboard_instance.main_leaderboard()
                elif choice == 'q':
                    general_user_flag = False
            self.output_menu_instance.quit()

    def login_or_register(self):

        login_choice = self.login()
        if login_choice == 'login' or login_choice == 'l':
            library = self.authentication()
            if library == 'q':
                self.output_menu_instance.quit()
            else:
                self.general_user_interface(library)
        elif login_choice == 'register' or login_choice == 'r':
            self.new_user_interface()

    def authentication(self):
        current_user_dictionary = self.database_accessing_library_instance.load_a_file('user_database')
        access = False
        username_tries = 0
        library = []

        while not access:
            if username_tries > 0:  # check if a username has been entered before
                print('try again')
                print('-' * 50)
            print('what is your username?'.center(50))
            username = input()  # ask username
            if username in current_user_dictionary['users'].keys():  # check if username is correct
                rank = 'users'
                flag = True
                ok = self.check_password(flag, rank, username, current_user_dictionary)
                if ok:
                    library = current_user_dictionary[rank][username]
                    access = True
            elif username in current_user_dictionary['admins'].keys():
                rank = 'admins'
                flag = True
                ok = self.check_password(flag, rank, username, current_user_dictionary)
                if ok:
                    library = current_user_dictionary[rank][username]
                    access = True

            elif username == 'q':
                return username

            username_tries += 1

        return library

    @staticmethod
    def check_password(flag, rank, username, current_user_dictionary):
        password_tries = 0
        while flag:
            if password_tries > 0:
                print('invalid input, try again'.center(50))
            print('-' * 50)
            print('what is your password?'.center(50))
            password = input()
            if current_user_dictionary[rank][username]['password'] == password:
                return True
            else:
                password_tries += 1
