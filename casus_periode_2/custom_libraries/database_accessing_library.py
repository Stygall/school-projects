import pickle

empty_dictionary = {}
user_database_backup = {'users': {'Miel': ['Miel.noelanders@zuyd.nl', 'mielisawesome',
                                           {'quiz': '', 'score': 0, 'codes': []}]},
                        'admins': {'Dev': ['Developer', 'test123']}}


class Dal:

    @staticmethod
    def save_a_file(reason, file_to_save_dictionary_to):
        filename = 'databases/' + reason + '_pickle.txt'
        with open(filename, 'wb') as file:
            pickle.dump(file_to_save_dictionary_to, file)

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


# class Scanner:
