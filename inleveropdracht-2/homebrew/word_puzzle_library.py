from homebrew import menu_library
from homebrew import database_library
from homebrew import word_library
from homebrew import registry_library
from difflib import SequenceMatcher
import random


class CrossWordPuzzle:

    puzzle_word_list = []
    complete_word_list = []
    previously_used_word_list = []
    user = ''
    question_language = ''
    answer_language = ''

    def __init__(self):

        self.output_menu_instance = menu_library.OutputMenus()
        self.dal_instance = database_library.Dal()
        self.word_instance = word_library.Word()
        self.registry_instance = registry_library.Creator()

    def start_session(self, library):

        self.output_menu_instance.start_crossword_session()
        reason = library[0] + '_training'
        self.dal_instance.load_a_file(reason)
        current_puzzle = self.registry_instance.register_puzzle(answer_language, library)
        self.gather_puzzle_words(current_puzzle)
        self.session_control(current_puzzle)
        start_flag = True
        while start_flag:
            start_flag = self.session_control(current_puzzle)
        self.output_menu_instance.quit()

    def session_control(self, current_puzzle):

        session_flag = True
        start = 0
        while session_flag:
            print('-'*50)
            update_list = self.ask_question(current_puzzle, start)
            if update_list[0]:
                print('hi')
            self.output_menu_instance.work_in_progress()
            session_flag = False
            start += 1

            return session_flag

    def print_puzzle(self, current_puzzle):

        for item in self.puzzle_word_list:
            if item[0]:
                print(item[current_puzzle.answer_language])
            if not item[0]:
                print('x')

    def gather_puzzle_words(self, current_puzzle):

        check_if_previous_flag = True

        reason = current_puzzle.user + '_training'
        dictionary = self.dal_instance.load_a_file(reason)
        if not current_puzzle.complete_word_list:
            current_puzzle.complete_word_list = self.word_instance.word_dictionary_to_list(dictionary)
        base_list = current_puzzle.complete_word_list
        new_list = []

        while check_if_previous_flag:
            word_index = random.randrange(0, (len(base_list) - 1))
            check_list = self.check_if_previous(word_index, base_list)
            okay = check_list[0]
            if okay == 1:
                check_if_previous_flag = True
            elif okay == 0:
                check_if_previous_flag = False
        current_puzzle.question_list = new_list

        return current_puzzle


    def ask_question(self, current_training, start):

        puzzle_word_list = current_training.puzzle_word_list
        if start == 0:
            self.previously_used_word_list = []

        check_if_previous_flag = True
        question_flag = True

    @staticmethod
    def check_answer(answer, correct_answer, question_list, question_index, start):

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
        previous = self.previously_used_word_list
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
