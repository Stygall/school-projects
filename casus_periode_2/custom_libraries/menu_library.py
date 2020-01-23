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

    @staticmethod
    def startup():

        print()
        print('-' * 50)
        print('welcome to QrUIZ'.center(50))
        print('-' * 50)
        print('enter Q at any time to stop the application'.center(50))
        print('-' * 50)

    @staticmethod
    def welcome_message(library):

        print('-' * 50)
        message = 'welcome ' + library[0]
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
    def new_user_interface(self):

        reason = 'user_database'
        user_database = self.database_accessing_library_instance.load_a_file(reason)
        original_user_dictionary = user_database['users']
        new_user = self.object_registry_instance.register_new_user()
        print(self.user_instance.user_object_to_list(new_user))
        print('continue')
        new_user_list = self.user_instance.user_object_to_list(new_user)
        new_user_dictionary = self.user_instance.user_list_to_dictionary(new_user, original_user_dictionary,
                                                                         new_user_list)
        self.database_accessing_library_instance.save_a_file(reason, new_user_dictionary)
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

        return choice

    def general_user_interface(self, library):

        self.output_menu_instance.welcome_message(library)
        general_user_flag = True
        while general_user_flag:
            self.output_menu_instance.main_menu()
            choice = input().lower()
            # if choice == 't':
            #     # self.quiz_instancestarwe.start_session(library)
            # elif choice == 'c':
            #     self.crossword_instance.start_session(library)
            if choice == 'q':
                general_user_flag = False
        self.output_menu_instance.quit()

    def login_or_register(self):

        login_choice = self.login()
        if login_choice.lower() == 'login':
            library = self.authentication()
            if library[0] == 'Dev':
                self.developer_instance.developer_console()
            elif library == 'q':
                self.output_menu_instance.quit()
            else:
                self.general_user_interface(library)
        elif login_choice.lower() == 'register':
            self.new_user_interface()

    def authentication(self):

        current_user_dictionary = self.database_accessing_library_instance.load_a_file('user_database')
        access = False
        username_tries = 0
        password_tries = 0
        library = []

        while not access:
            if username_tries > 0:  # check if a username has been entered before
                print('try again')
                print('-' * 50)
            print('what is your username?'.center(50))
            username = input() # ask username
            if username in current_user_dictionary['users'].keys():  # check if username is correct
                rank = 'users'
                flag = True
            elif username in current_user_dictionary['admins'].keys():
                rank = 'admins'
                flag = True
            elif username == 'q':
                return username
            while flag:
                if password_tries > 0:
                    print('invalid input, try again'.center(50))
                print('-' * 50)
                print('what is your password?'.center(50))
                password = input()
                if current_user_dictionary[rank][username][1] == password:
                    library = current_user_dictionary[rank][username]
                    access = True
                    flag = False
                else:
                    password_tries += 1

            username_tries += 1

        return library


