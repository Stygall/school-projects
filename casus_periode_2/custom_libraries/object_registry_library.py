from custom_libraries import database_accessing_library
from custom_libraries import user_library
from custom_libraries import menu_library


class Creator:

    def __init__(self):
        self.database_accessing_library_instance = database_accessing_library.Dal()
        self.user_instance = user_library.User()
        self.output_menu_instance = menu_library.OutputMenus()

    def register_new_user(self):

        base = self.database_accessing_library_instance.load_a_file('user_database')
        new_user = self.user_instance
        username_flag = False
        while not username_flag:
            new_user.name = input('please give us a username: ')
            if new_user.name in base.keys():
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

        print(new_user.name,
              new_user.password,
              new_user.email,
              new_user.quiz)
        input()
        return new_user
