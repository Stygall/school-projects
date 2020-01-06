import pickle


def load_a_file(reason):
    filename = reason + '_pickle.txt'
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

reason = input('filename')
readpickle = load_a_file(reason)
print(readpickle)