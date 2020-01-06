from homebrew import word_library
from homebrew import database_library
from homebrew import user_library
from homebrew import menu_library
from homebrew import word_training_library
from homebrew import word_puzzle_library


class Creator:

    def __init__(self):
        self.dal_instance = database_library.Dal()
        self.word_instance = word_library.Word()
        self.user_instance = user_library.User()
        self.output_menu_instance = menu_library.OutputMenus()
        self.option = ''

    def register_new_word(self):
        new_word = self.word_instance
        register_new_word_flag = True
        while register_new_word_flag:
            print('what is the dutch translation?'.center(50))
            new_word.dictionary_key = input()
            print('what is the english translation?'.center(50))
            english = input()
            print('-' * 50)
            print('are these correct? \ndutch: ' + new_word.dictionary_key + '\nenglish: ' + english)
            choice = input()
            if choice == 'yes':
                new_word.english = english
                register_new_word_flag = False
            else:
                print('try again'.center(50))
        new_word.factor = 5

        return new_word

    def register_new_user(self):
        new_user = self.user_instance
        new_user.name = input('what is your name? ')
        new_user_flag = True
        while new_user_flag:
            print('choose from these trainings:')
            print('1 = English to Dutch')
            print('2 = Dutch to english')
            choice = input()
            if choice == '1':
                new_user.trainingList.append('en_nl')
                new_user_flag = False
            elif choice == '2':
                new_user.trainingList.append('nl_en')
                new_user_flag = False
            else:
                print('invalid input, try again'.center(50))
        print('enter your password below')
        new_user.password = input()
        return new_user

    def register_training(self, library):

        new_training = word_training_library.VocabularyTrainer()
        new_training.user = library[0]

        print('-' * 50)
        print('what language do you want to practice?'.center(50))

        def choose_answer_language(library):
            for item in library[2]:
                print(item)
                print('do you want to practice this language?'.center(50))
                choose_answer_language_flag = True

                while choose_answer_language_flag:
                    print('(y)es or (n)o?'.center(50))
                    choice = input().lower()
                    if choice.lower() == 'y':
                        new_training.answer_language = library[2].index(item) + 1
                        return new_training
                    elif choice.lower() == 'n':
                        choose_answer_language_flag = False
                    elif choice.lower() == 'q':
                        choose_answer_language_flag = False
                        self.output_menu_instance.quit()
                    else:
                        print('invalid input please try again'.center(50))

        def choose_question_language(library):

            part_three_flag = True

            print('-' * 50)
            print('what language do you want be questioned with?'.center(50))

            while part_three_flag:
                for item in library[2]:
                    print(item)
                    print('do you want to be questioned with this language?'.center(50))
                    choose_answer_language_flag = True

                    while choose_answer_language_flag:
                        print('(y)es or (n)o?'.center(50))
                        choice = input().lower()
                        if choice.lower() == 'y':
                            new_training.question_language = library[2].index(item) + 1
                            return new_training
                        elif choice.lower() == 'n':
                            choose_answer_language_flag = False
                        elif choice.lower() == 'q':
                            choose_answer_language_flag = False
                            part_three_flag = False
                            self.output_menu_instance.quit()
                        else:
                            print('invalid input please try again'.center(50))
        choose_answer_language(library)
        choose_question_language(library)
        print(new_training.question_language)
        return new_training

    def register_puzzle(self, library):
        new_training = word_puzzle_library.CrossWordPuzzle()
        new_training.user = library[0]

        part_one_flag = True
        part_two_flag = True
        part_three_flag = True

        print('-' * 50)
        print('what language do you want to practice?'.center(50))
        while part_one_flag:
            for item in library[2]:
                print(item)
                print('do you want to practice this language?'.center(50))
                choose_answer_language_flag = True
                while choose_answer_language_flag:
                    print('(y)es or (n)o?'.center(50))
                    choice = input().lower()
                    if choice.lower() == 'y':
                        new_training.answer_language = library[2].index(item) + 1
                        choose_answer_language_flag = False
                        part_one_flag = False
                    elif choice.lower() == 'n':
                        choose_answer_language_flag = False
                    elif choice.lower() == 'q':
                        choose_answer_language_flag = False
                        part_three_flag = False
                        part_two_flag = False
                        self.output_menu_instance.quit()
                    else:
                        print('invalid input please try again'.center(50))

        while part_two_flag:
            index = new_training.answer_language - 1
            library[2].pop(index)
            question_language_options = library[2]
            if len(question_language_options) == 1:
                new_training.question_language = library[0]
            else:
                print('-' * 50)
                print('what language do you want be questioned with?'.center(50))

                while part_three_flag:
                    for item in library[2]:
                        print(item)
                        print('do you want to be questioned with this language?'.center(50))
                        choose_answer_language_flag = True

                        while choose_answer_language_flag:
                            print('(y)es or (n)o?'.center(50))
                            choice = input().lower()
                            if choice.lower() == 'y':
                                new_training.question_language = library[2].index(item) + 1
                                return new_training
                            elif choice.lower() == 'n':
                                choose_answer_language_flag = False
                            elif choice.lower() == 'q':
                                choose_answer_language_flag = False
                                part_three_flag = False
                                part_two_flag = False
                                self.output_menu_instance.quit()
                            else:
                                print('invalid input please try again'.center(50))
