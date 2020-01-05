from homebrew import database_library

dal_instance = database_library.Dal()
word_dict = dal_instance.load_a_file('word')


class Word:
    dictionary_key = ''
    dutch = dictionary_key
    factor = ''
    english = ''

    def word_object_to_list(self):
        word_list = [self.factor, self.dictionary_key, self.english]
        return word_list

    def word_list_to_dictionary(self, original_word_dictionary, word_list):
        original_word_dictionary[self.dictionary_key] = word_list
        return original_word_dictionary

    @staticmethod
    def word_dictionary_to_list(read_pickle):
        words = []
        for var in read_pickle.keys():
            words.append(read_pickle[var])
        return words

    @staticmethod
    def word_list_to_objects(words):
        new_word = Word()
        for item in words:
            new_word.factor = item[0]
            new_word.english = item[2]
            new_word.dictionary_key = item[1]
