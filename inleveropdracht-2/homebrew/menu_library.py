from homebrew import word_library
from homebrew import database_library
from homebrew import registry_library
from homebrew import user_library
from homebrew import word_training_library
from homebrew import word_puzzle_library
from homebrew import developer_library


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
        print('welcome to LingoSim'.center(50))
        print('-' * 50)
        print('enter Q at any time to stop the application'.center(50))
        print('-' * 50)

    @staticmethod
    def welcome_message(library):

        print('-' * 50)
        message = 'welcome ' + library[0]
        print(message.center(50))

    @staticmethod
    def start_training_session():

        print('-' * 50)
        print('your training session is about to start'.center(50))
        print('3'.center(50))
        print('2'.center(50))
        print('1'.center(50))
        print('GO!'.center(50))
        print('type "Q" as answer to quit'.center(50))

    @staticmethod
    def start_crossword_session():

        print('-' * 50)
        print('your crossword session is about to start'.center(50))
        print('3'.center(50))
        print('2'.center(50))
        print('1'.center(50))
        print('GO!'.center(50))
        print('type "Q" as answer to quit'.center(50))

    @staticmethod
    def work_in_progress():

        print('-'*50)
        print('this functionality is not fully operational yet,'.center(50))
        print('please try again later'.center(50))
        print('-'*50)

    @staticmethod
    def quit():

        print('see you next time!')

    @staticmethod
    def ask_question_from_training(question):

        print('give the correct translation of the following word:'.center(50))
        print(question)

    @staticmethod
    def developer_options():

        print('-'*50)
        print('the following are your options:')
        print('add-word, which lets you add a word')
        print('reset-words, which resets to default')
        print('reset-users, which resets to default')
        print('nuke, which resets all files')
        print('add-language, which lets you add a new language')
        print('main, which returns you to the default menu')

    @staticmethod
    def main_menu():

        print('-'*50)
        print('do you want to start a (t)raining?'.center(50))
        print('or'.center(50))
        print('do you want to make a (c)ross-word puzzle?'.center(50))
        print('or'.center(50))
        print('do you want to (q)uit?'.center(50))
        print('-' * 50)


class InputMenus:

    def __init__(self):

        self.dal_instance = database_library.Dal()
        self.word_instance = word_library.Word()
        self.registry_instance = registry_library.Creator()
        self.user_instance = user_library.User()
        self.output_menu_instance = OutputMenus()
        self.training_instance = word_training_library.VocabularyTrainer()
        self.crossword_instance = word_puzzle_library.CrossWordPuzzle()
        self.developer_instance = developer_library.Developer()

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
            if choice == 't':
                self.training_instance.start_session(library)
            elif choice == 'c':
                self.crossword_instance.start_session(library)
            elif choice == 'q':
                general_user_flag = False
        self.output_menu_instance.quit()

    def new_user_interface(self):

        reason = 'user'
        original_user_dictionary = self.dal_instance.load_a_file(reason)
        new_user = self.registry_instance.register_new_user()
        print(self.user_instance.user_object_to_list(new_user))
        print('continue')
        new_user_list = self.user_instance.user_object_to_list(new_user)
        new_user_dictionary = self.user_instance.user_list_to_dictionary(new_user, original_user_dictionary,
                                                                         new_user_list)
        self.dal_instance.save_a_file(reason, new_user_dictionary)
        print('-' * 50)
        print('your account has been successfully registered!'.center(50))
        print('please log in to the application')
        library = self.authentication()
        self.general_user_interface(library)

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

        current_user_dictionary = self.dal_instance.load_a_file('user')
        access = False
        username_tries = 0
        password_tries = 0
        library = []

        while not access:
            if username_tries > 0:
                print('try again')
                print('-' * 50)
            print('what is your username?'.center(50))
            username = input()
            for var in current_user_dictionary.keys():
                if var == username:
                    flag = True
                    while flag:
                        if password_tries > 0:
                            print('invalid input, try again'.center(50))
                        print('-' * 50)
                        print('what is your password?'.center(50))
                        password = input()
                        if current_user_dictionary[username][1] == password:
                            library = current_user_dictionary[username]
                            access = True
                            flag = False
                        elif password == 'q':
                            return password
                        else:
                            password_tries += 1
                elif username == 'q':
                    return username
            username_tries += 1

        return library
