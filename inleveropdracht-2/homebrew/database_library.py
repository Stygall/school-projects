import pickle

word_dictionary_backup = {'brood': [5, 'brood', 'bread'],
                          'zelfmoord': [5, 'zelfmoord', 'suicide'],
                          'broodrooster': [5, 'broodrooster', 'toaster'],
                          'badkuip': [5, 'badkuip', 'bathtub'],
                          'pindakaas': [5, 'pindakaas', 'peanutbutter'],
                          'jam': [5, 'jam', 'jelly'],
                          'augurk': [5, 'augurk', 'pickle'],
                          'handtas': [5, 'handtas', 'purse'],
                          'voordeur': [5, 'voordeur', 'front door'],
                          'kestboom': [5, 'kerstboom', 'christmas tree']
                          }

user_dictionary_backup = {'Miel': ['Miel', 'mielisawesome', ['nl_en', 'en_nl']], 'Dev': ['Dev', 'test123']}


class Dal:

    @staticmethod
    def save_a_file(reason, file_to_save_dictionary_to):
        filename = 'application_data/' + reason + '_pickle.txt'
        with open(filename, 'wb') as file:
            pickle.dump(file_to_save_dictionary_to, file)

    @staticmethod
    def load_a_file(reason):
        filename = 'application_data/' + reason + '_pickle.txt'
        try:
            with open(filename, 'rb') as file:
                read_pickle = pickle.load(file)
            return read_pickle
        except FileNotFoundError:
            with open(filename, 'wb') as file:
                if '_' in filename:
                    pickle.dump(word_dictionary_backup, file, pickle.HIGHEST_PROTOCOL)
                    file.close()
            with open(filename, 'rb') as file:
                read_pickle = pickle.load(file)
            return read_pickle
