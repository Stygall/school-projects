from homebrew import menu_library
from homebrew import database_library
from homebrew import registry_library
from homebrew import word_library
import random
from difflib import SequenceMatcher


class WordTrainer:
    question_list = []
    base_list = []
    user = ''
    question_language = ''
    answer_language = ''
    previous_word_list = []

    def __init__(self):
        self.output_menu_instance = menu_library.OutputMenus()
        self.dal_instance = database_library.Dal()
        self.registry_instance = registry_library.Creator()
        self.word_instance = word_library.Word()

    def start_session(self, library):
        self.output_menu_instance.start_training_session()
        reason = library[0] + '_training'
        self.dal_instance.load_a_file(reason)
        # defining which in language the user will answer
        answer_language = menu_library.InputMenus.choose_language(self)
        # defining the current training
        current_training = self.registry_instance.register_training(answer_language, library)
        #
        current_training = self.make_base_list_and_question_list(current_training)
        flag = True
        while flag:
            flag = self.session_control(current_training)

    def session_control(self, current_training):
        session_flag = True
        start = 0
        while session_flag:
            print('-' * 50)
            update_list = self.ask_question(current_training, start)
            if update_list[4] == 'q':
                if not update_list[4]:
                    session_flag = False
            self.update_base_list(current_training, update_list)
            print(current_training.question_list)
            start = update_list[3]
            start += 1
        if not session_flag:
            reason = current_training.user + '_training'
            x = self.dal_instance.load_a_file(reason)
            self.word_instance.word_list_to_dictionary(x, self.question_list)
            self.dal_instance.save_a_file(reason, current_training.question_list)
        return session_flag

    def make_base_list_and_question_list(self, current_training):
        reason = current_training.user + '_training'
        dictionary = self.dal_instance.load_a_file(reason)
        base_list = current_training.base_list
        if not base_list:
            base_list = self.word_instance.word_dictionary_to_list(dictionary)
        new_list = []
        for item in base_list:
            x = 0
            while x < item[0]:
                new_list.append(item)
                x += 1
        current_training.question_list = new_list
        return current_training

    @staticmethod
    def update_base_list(current_training, update_list):
        correct = update_list[0]
        word = update_list[2]
        base_list = current_training.base_list
        question_list = current_training.question_list
        if correct:
            if word in base_list:
                index = base_list.index(word)
                factor = base_list[index][0]
                factor -= 1
                new_index = question_list.index(word)
                question_list.pop(new_index)
                return current_training
        elif not correct:
            if word in base_list:
                index = base_list.index(word)
                factor = base_list[index][0]
                factor += 1
                question_list.append(word)
                return current_training

    def ask_question(self, current_training, start):
        question_list = current_training.question_list
        if start == 0:
            self.previous_word_list = []
        check_if_previous_flag = True
        question_flag = True

        while question_flag:
            # checking if the chosen word has been asked before
            question_index = 0
            while check_if_previous_flag:
                question_index = random.randrange(0, (len(question_list) - 1))
                check_list = self.check_if_previous(question_index, question_list)
                okay = check_list[0]
                if okay == 1:
                    check_if_previous_flag = True
                elif okay == 0:
                    check_if_previous_flag = False

            item = question_list[question_index]
            self.previous_word_list.append(item)

            if len(self.previous_word_list) > 4:
                self.previous_word_list.pop(0)

            correct_answer = question_list[question_index][current_training.answer_language]
            question = question_list[question_index][current_training.question_language]

            self.output_menu_instance.ask_question_from_training(question)

            answer = input()
            # when the answer is entirely correct
            if answer == correct_answer.lower():
                print('your answer is correct!'.center(50))
                correct = True
                factor = question_list[question_index][0]
                word = question_list[question_index][1]
                start += 1
                update_list = [correct, factor, word, start, True]
                return update_list
            # when the answer is q
            elif answer.lower() == 'q':
                factor = question_list[question_index][0]
                word = question_list[question_index][1]
                correct = answer
                start += 1
                update_list = [correct, factor, word, start, False]
                return update_list
            # when the answer had incorrect capitalisation
            elif answer.lower() == correct_answer.lower():
                print('your answer is not entirely correct'.center(50))
                print('Pay close attention to your capitalisation'.center(50))
                correct = False
                factor = question_list[question_index][0]
                word = question_list[question_index][1]
                start += 1
                update_list = [correct, factor, word, start, True]
                return update_list
            # when the answer had a small spelling mistake
            elif SequenceMatcher(None, answer, correct_answer).ratio() >= 0.75:
                print('your answer is not entirely correct'.center(50))
                print('please watch your spelling next time'.center(50))
                correct = False
                factor = question_list[question_index][0]
                word = question_list[question_index][1]
                start += 1
                update_list = [correct, factor, word, start, True]
                return update_list
            # when the answer is entirely incorrect
            else:
                print('your answer is not correct'.center(50))
                print('please try again'.center(50))
                correct = False
                factor = question_list[question_index][0]
                word = question_list[question_index][1]
                start += 1
                update_list = [correct, factor, word, start, True]
                return update_list

    def check_if_previous(self, index, question_list):
        check_list = []
        item = question_list[index]
        previous = self.previous_word_list
        if item in previous:
            ok = 1
            check_list.append(ok)
            return check_list
        elif not previous:
            ok = 0
            check_list.append(ok)
            return check_list
        else:
            ok = 0
            if len(previous) >= 5:
                previous.pop(0)
                check_list.append(ok)
                return check_list
            else:
                check_list.append(ok)
                return check_list
