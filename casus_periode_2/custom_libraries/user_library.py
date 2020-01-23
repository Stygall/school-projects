from custom_libraries import database_accessing_library


class User:

    username = ''
    password = ''
    email = ''
    quiz = {'score': 0, 'codes': []}

    @staticmethod
    def user_object_to_list(new_user):
        user_list = [new_user.email, new_user.password, new_user.score]
        return user_list

    @staticmethod
    def user_list_to_dictionary(original_user_dictionary, user_list, new_user):
        original_user_dictionary[new_user.name] = user_list
        print(original_user_dictionary)
        return original_user_dictionary


class Admin(User):

    def __init_subclass__(cls, **kwargs):
        print('hello')
