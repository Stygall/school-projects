from homebrew import word_library
from homebrew import database_library
from homebrew import registry_library
from homebrew import user_library
from homebrew import word_training_library
from homebrew import word_puzzle_library


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
        # print('-' * 50)
        print('give the correct translation of the following word:'.center(50))
        print(question)


class InputMenus:

    def __init__(self):
        self.dal_instance = database_library.Dal()
        self.word_instance = word_library.Word()
        self.registry_instance = registry_library.Creator()
        self.user_instance = user_library.User()
        self.output_menu_instance = OutputMenus()
        self.training_instance = word_training_library.WordTrainer()
        self.crossword_instance = word_puzzle_library.CrossWord()

    @staticmethod
    def login():
        flag = True
        choice = ''
        while flag:
            print('do you want to login or register?'.center(50))
            choice = input()
            if choice.lower() == 'login' or choice == 'register':
                flag = False
            elif choice.lower() == 'q':
                OutputMenus.quit()
            else:
                print('invalid input, try again'.center(50))
            print('-' * 50)
        return choice

    def developer_console(self):
        developer_flag = True
        while developer_flag:
            developer_choice = input('... ')
            print('-' * 50)
            if developer_choice.lower() == 'reset-users':
                self.dal_instance.save_a_file('user', database_library.user_dictionary_backup)
            elif developer_choice.lower() == 'reset-words':
                self.dal_instance.save_a_file('word', database_library.word_dictionary_backup)
            elif developer_choice.lower() == 'add-word':
                original_word_dictionary = self.dal_instance.load_a_file('word')
                new_word = self.registry_instance.register_new_word()
                new_word_list = self.word_instance.word_object_to_list(new_word)
                new_word_dictionary = self.word_instance.word_list_to_dictionary(new_word, original_word_dictionary, new_word_list)
                reason = input('give the filename without "Pickle.txt: "')
                new = self.dal_instance.save_a_file(reason, new_word_dictionary)
                print(new)
            elif developer_choice.lower() == 'nuke':
                confirmation = input('are you sure? ')
                if confirmation.lower() == 'yes':
                    current_user_database = self.dal_instance.load_a_file('user')
                    current_word_database = self.dal_instance.load_a_file('word')
                    for var in current_user_database.keys():
                        reason = var + '_training'
                        self.dal_instance.save_a_file(reason, current_word_database)
                    for var in current_user_database.keys():
                        reason = var + '_training'
                        self.dal_instance.save_a_file(reason, current_word_database)
                elif confirmation.lower() == 'q':
                    self.output_menu_instance.quit()
            elif developer_choice.lower() == 'q':
                self.output_menu_instance.quit()
                developer_flag = False
            elif developer_choice.lower() == 'main':
                developer_flag = False
        self.login_or_register()

    def general_user_interface(self, library):
        self.output_menu_instance.welcome_message(library)
        general_user_flag = True
        while general_user_flag:
            print('do you want to start a (t)raining?'.center(50))
            print('or'.center(50))
            print('do you want to make a (c)ross-word puzzle?'.center(50))
            print('or'.center(50))
            print('do you want to (q)uit?'.center(50))
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
        new_user_dictionary = self.user_instance.user_list_to_dictionary(new_user, original_user_dictionary, new_user_list)
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
                self.developer_console()
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
                            self.output_menu_instance.quit()
                        else:
                            password_tries += 1
                elif username == 'q':
                    self.output_menu_instance.quit()
            username_tries += 1
        return library

    def choose_language(self):
        print('-' * 50)
        print('what language do you want to practice?'.center(50))
        print('(d)utch?'.center(50))
        print('or'.center(50))
        print('(e)nglish?'.center(50))
        choice = input().lower()
        # flag = True
        # while flag:
        if choice == 'd':
            answer_language = 1
            return answer_language
        elif choice == 'e':
            answer_language = 2
            return answer_language
        elif choice == 'q':
            self.output_menu_instance.quit()
