from custom_libraries import menu_library
from custom_libraries import user_library
from custom_libraries import database_accessing_library


class Quiz:

    answer = ''
    question = ''
    value = ''
    user = {}
    quiz = ''
    code = ''

    def __init__(self):

        self.output_menu_instance = menu_library.OutputMenus()
        self.user_instance = user_library.User()
        self.database_accessing_instance = database_accessing_library.Dal()

    def ask_question(self, new_quiz):

        self.output_menu_instance.ask_question(new_quiz.question)
        print('what is the answer?'.center(50))
        given_answer = input()
        correct = self.check_answer(given_answer, new_quiz)
        if correct:
            database = self.update_profile(new_quiz)
            print(database)
            input()
            self.database_accessing_instance.save_a_file('user_database', database)

    @staticmethod
    def check_answer(given_answer, new_quiz):

        if given_answer == new_quiz.answer:
            print("that's correct!".center(50))
            return True
        else:
            print('unfortunately,\n that was the wrong answer'.center(50))
            return False

    def update_profile(self, new_quiz):

        new_score = new_quiz.value
        database = self.database_accessing_instance.load_a_file('user_database')
        database['users'][new_quiz.user['username']]['score'] += new_score
        quiz = new_quiz.quiz
        if not database['users'][new_quiz.user['username']]['quiz'] == quiz:
            database['users'][new_quiz.user['username']]['quiz'] = quiz
        code = new_quiz.code
        if not database['users'][new_quiz.user['username']]['codes'] == code:
            database['users'][new_quiz.user['username']]['codes'].append(code)
        return database


class Question:

    code = ''
    quiz = ''
    question = ''
    answer = ''
    value = 0
    writer = ''

    @staticmethod
    def question_object_to_dictionary(original_question_dictionary, question):
        original_question_dictionary[question.code] = {'code': question.code,
                                                       'quiz': question.quiz,
                                                       'writer': question.writer,
                                                       'question': question.question,
                                                       'answer': question.answer,
                                                       'value': question.value}
        return original_question_dictionary

    def choose_question(self, library):
        edited_question = Question()
        current_writer = library['username']
        code_list = []
        base_code_dictionary = self.database_accessing_library_instance.load_a_file('question_database')
        for item in base_code_dictionary:
            code_list.append(item['code'])

        for item in code_list:
            print('-' * 50)
            print(item)
            print('do you want to change this code?')
            ask = input().lower()
            print('-' * 50)

            if ask == 'yes' or ask == 'y':
                chosen_question = base_code_dictionary[item]

                def change_question(library, chosen_question):
                    print('-' * 50)
                    print('what do you want to change?')
                    print('(q)uestion:')
                    print(chosen_question['question'])
                    print('(a)nswer:')
                    print(chosen_question['answer'])
                    print('(v)alue:')
                    print(chosen_question['value'])
                    print('-' * 50)

                    edit_choice = input().lower()
                    question_flag = True
                    answer_flag = True
                    value_flag = True
                    choosing = True
                    while choosing:
                        if edit_choice == 'q':
                            while question_flag:
                                print('please give a new question:')
                                new_item = input()
                                print(new_item)
                                print('is this correct?')
                                ok = input().lower()

                                if ok == 'yes' or ok == 'y':
                                    extra = [new_item, 'answer', chosen_question]
                                    return extra

                                elif ok == 'no' or ok == 'n':
                                    print('ok, please try again then.')

                                elif ok == 'q':
                                    menu_library.OutputMenus.quit()

                        elif edit_choice == 'a':
                            while answer_flag:
                                print('please give a new answer:')
                                new_item = input()
                                print(new_item)
                                print('is this correct?')
                                ok = input().lower()

                                if ok == 'yes' or ok == 'y':
                                    extra = [new_item, 'answer', chosen_question]
                                    return extra

                                elif ok == 'no' or ok == 'n':
                                    print('ok, please try again then.')

                                elif ok == 'q':
                                    menu_library.OutputMenus.quit()

                        elif edit_choice == 'v':
                            while value_flag:
                                print('please give a new value:')
                                new_item = input()
                                print(new_item)
                                print('is this correct?')
                                ok = input().lower()

                                if ok == 'yes' or ok == 'y':
                                    extra = [new_item, 'answer', chosen_question]
                                    return extra

                                elif ok == 'no' or ok == 'n':
                                    print('ok, please try again then.')

                                elif ok == 'q':
                                    menu_library.OutputMenus.quit()

                extra = change_question(library, chosen_question)

                if extra[1] == 'question':
                    chosen_question['quesiton'] = extra[0]
                elif extra[1] == 'answer':
                    chosen_question['answer'] = extra[0]
                elif extra[1] == 'value':
                    chosen_question['value'] = extra[0]
                return chosen_question
