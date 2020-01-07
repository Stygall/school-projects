from homebrew import database_library
from homebrew import menu_library
from homebrew import registry_library
from homebrew import word_library


class Developer:

    def __init__(self):

        self.dal_instance = database_library.Dal()
        self.output_menu_instance = menu_library.OutputMenus()
        self.registry_instance = registry_library.Creator()
        self.word_instance = word_library.Word()

    def developer_console(self):

        developer_flag = True
        while developer_flag:
            self.output_menu_instance.developer_options()
            developer_choice = input('... ')
            print('-' * 50)
            if developer_choice.lower() == 'reset-users':
                self.reset_users()
            elif developer_choice.lower() == 'reset-words':
                self.reset_words()
            elif developer_choice.lower() == 'add-word':
                self.add_word()
            elif developer_choice.lower() == 'nuke':
                confirmation = input('are you sure? ')
                if confirmation.lower() == 'yes':
                    self.nuke()
                elif confirmation.lower() == 'q':
                    self.output_menu_instance.quit()
                    developer_flag = False
            elif developer_choice.lower() == 'add-language':
                self.output_menu_instance.work_in_progress()
                # self.add_language()
            elif developer_choice.lower() == 'q':
                developer_flag = False
                self.output_menu_instance.quit()

            elif developer_choice.lower() == 'main':
                developer_flag = False
                self.back_to_main_menu()

    def reset_users(self):

        self.dal_instance.save_a_file('user', database_library.user_dictionary_backup)

    def reset_words(self):

        self.dal_instance.save_a_file('word', database_library.word_dictionary_backup)

    def add_word(self):

        original_word_dictionary = self.dal_instance.load_a_file('word')
        new_word = self.registry_instance.register_new_word()
        new_word_list = new_word.word_object_to_list()
        new_word_dictionary = new_word.word_list_to_dictionary(original_word_dictionary,
                                                               new_word_list)
        reason = input('give the filename without "_Pickle.txt: "')
        self.dal_instance.save_a_file(reason, new_word_dictionary)

    def nuke(self):

        current_user_database = self.dal_instance.load_a_file('user')
        current_word_database = self.dal_instance.load_a_file('word')
        for var in current_user_database.keys():
            reason = var + '_training'
            self.dal_instance.save_a_file(reason, current_word_database)
        for var in current_user_database.keys():
            reason = var + '_training'
            self.dal_instance.save_a_file(reason, current_word_database)

    def add_language(self):

        print('-'*50)
        old_word_dictionary = self.dal_instance.load_a_file('word')
        old_word_list = self.word_instance.word_dictionary_to_list(old_word_dictionary)
        print('what is the new language?'.center(50))
        new_language = input().lower()
        for item in old_word_list:
            new_translation = ''
            allowed = False
            print(item)
            print('what is the', new_language, 'translation?'.center(50))
            while not allowed:
                new_translation = input()
                print('is this correct?'.center(50))
                print(new_translation)
                choice = input()
                if choice.lower() == 'yes' or 'y':
                    allowed = True
                else:
                    print('invalid input, please try again'.center(50))
            item.append(new_translation)
        self.word_instance.other_word_list_to_dictionary(old_word_dictionary, old_word_list)

    @staticmethod
    def back_to_main_menu():

        input_menu_instance = menu_library.InputMenus()
        menu_library.InputMenus.login_or_register(input_menu_instance)