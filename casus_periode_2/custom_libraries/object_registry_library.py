from custom_libraries import database_accessing_library
from custom_libraries import user_library
from custom_libraries import menu_library
from custom_libraries import quiz_library


class Creator:

    def __init__(self):

        self.database_accessing_library_instance = database_accessing_library.Dal()
        self.user_instance = user_library.User()
        self.output_menu_instance = menu_library.OutputMenus()
        self.quiz_instance = quiz_library.Quiz()
        self.question_instance = quiz_library.Question()

    def register_new_user(self):

        base = self.database_accessing_library_instance.load_a_file('user_database')
        new_user = self.user_instance
        username_flag = False
        while not username_flag:
            new_user.username = input('please give us a username: ')
            if new_user.username in base.keys():
                print('this username already exists, please choose another one.')
            else:
                username_flag = True
        password_flag = False
        while not password_flag:
            new_user.password = input('please give us a password: ')
            check_password = input('pleas confirm your password: ')
            if new_user.password == check_password:
                password_flag = True
            else:
                print('please try again, the passwords did not match')

        email_flag = False
        while not email_flag:
            new_user.email = input('please give us an email: ').lower()
            if '@' in new_user.email and '.' in new_user.email:
                email_flag = True
            else:
                print('this email is invalid, please try again')

        return new_user

    def register_new_quiz(self, scanned_code, library):

        new_quiz = self.quiz_instance
        base_code_dictionary = self.database_accessing_library_instance.load_a_file('question_database')
        scanned_code_dictionary = base_code_dictionary[scanned_code]
        new_quiz.question = scanned_code_dictionary['question']
        new_quiz.value = scanned_code_dictionary['value']
        new_quiz.answer = scanned_code_dictionary['answer']
        new_quiz.user = library
        new_quiz.quiz = scanned_code_dictionary['quiz']
        new_quiz.code = scanned_code
        return new_quiz

    def register_new_question(self, amount, library):

        current_writer = library['username']
        new_question = self.question_instance
        code_list = []
        base_code_dictionary = self.database_accessing_library_instance.load_a_file('question_database')
        if amount == 'all':
            print('retrieving all codes...'.center(50))
            for item in base_code_dictionary:
                code_list.append(item['code'])

        else:
            print('what code,\n do you want to use for the new question?'.center(50))
            print('choose from the following list'.center(50))
            for item in base_code_dictionary.keys():
                print(item)
                code_list.append(item)
            choosing_flag = False
            while not choosing_flag:
                choice = input()
                if choice in code_list:
                    chosen_code = choice
                    new_question.code = chosen_code
                    choosing_flag = True
                else:
                    print('this code does not exist\n please try again'.center(50))

        def define_question(new_question):

            ok = False
            while not ok:
                question_list = []
                print('what is the question?'.center(50))
                question = input()
                question_list.append(question)
                print('what is the answer?'.center(50))
                answer = input()
                question_list.append(answer)
                print('what is the score value?'.center(50))
                value = input()
                question_list.append(value)
                print('what is the quiz it belongs to?'.center(50))
                quiz = input()

                question_list.append(quiz)
                for question_item in question_list:
                    print(question_item)

                print('is all of this correct?'.center(50))
                question_choice = input()
                if question_choice.lower() == 'yes' or question_choice.lower() == 'y':
                    ok = True
                else:
                    print('let us start over then.'.center(50))

            new_question.quiz = question_list[3]
            new_question.answer = question_list[1]
            new_question.question = question_list[0]
            new_question.value = question_list[2]

            return new_question

        def give_signature(current_writer, new_question):
            new_question.writer = current_writer

            return new_question

        define_question(new_question)
        give_signature(current_writer, new_question)

    def admin_object(self, library):
        new_admin = user_library.Admin()
        new_admin.username = library['username']
        new_admin.password = library['password']
        new_admin.email = library['email']
        new_admin.rank = library['rank']
