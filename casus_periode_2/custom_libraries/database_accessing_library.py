import pickle
from custom_libraries import menu_library

empty_dictionary = {}
user_database_backup = {'users': {'Miel': {'username': 'Miel',
                                           'email': 'Miel.noelanders@zuyd.nl',
                                           'password': 'mielisawesome',
                                           'quiz': '',
                                           'score': 0,
                                           'codes': []}},
                        'admins': {'Developer': {'rank': 'developer',
                                                 'username': 'Developer',
                                                 'email': 'support@qruiz.com',
                                                 'password': 'test123'},
                                   'Admin01': {'rank': 'admin',
                                              'username': 'Admin01',
                                               'email': 'admin01@qruiz.com',
                                              'password': ''}}}
question_database_backup = {"QZ21": {'code': 'QZ21',
                                     "quiz": 'jan2020',
                                     'writer': 'Admin01',
                                     "question": 'Wie was de eerste koning van Nederland?',
                                     'answer': 'Lodewijk Bonaparte',
                                     'value': 10},
                            "QZ22": {'code': 'QZ22',
                                     "quiz": 'jan2020',
                                     'writer': 'Admin01',
                                     "question": 'Wat is het aboslute nulpunt?',
                                     'answer': '0 kelvin',
                                     'value': 10}}


class Dal:

    @staticmethod
    def save_a_file(reason, data):
        filename = 'databases/' + reason + '_pickle.txt'
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_a_file(reason):
        filename = 'databases/' + reason + '_pickle.txt'
        try:
            with open(filename, 'rb') as file:
                read_pickle = pickle.load(file)
            return read_pickle
        except FileNotFoundError:
            with open(filename, 'wb') as file:
                if '_' in filename:
                    pickle.dump(empty_dictionary, file, pickle.HIGHEST_PROTOCOL)
                    file.close()
            with open(filename, 'rb') as file:
                read_pickle = pickle.load(file)
            return read_pickle


class Scanner:

    def __init__(self):
        self.output_menu_instance = menu_library.OutputMenus()

    def scan_a_code(self, library):

        scan_flag = True
        while scan_flag:
            question_database = Dal.load_a_file('question_database')
            given_code = input("Please give a code to get a question: ")
            if given_code in question_database:
                ok = self.check_a_code(library, given_code)
                if ok:
                    scan_flag = False

                else:
                    self.output_menu_instance.wrong_question()
            else:
                print('this question does not exist, \n please try again'.center(50))

        return given_code

    @staticmethod
    def check_a_code(library, given_code):
        if given_code in library['codes']:
            return False
        else:
            return True
