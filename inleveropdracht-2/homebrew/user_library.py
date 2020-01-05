from homebrew import database_library

pickleInstance = database_library.Dal()
userDict = pickleInstance.load_a_file('user')


class User:
    name = ''
    password = ''
    trainingList = []

    @staticmethod
    def user_object_to_list(new_user):
        user_list = [new_user.name, new_user.password, new_user.trainingList]
        return user_list

    @staticmethod
    def user_list_to_dictionary(original_user_dictionary, user_list, new_user):
        original_user_dictionary[new_user.name] = user_list
        print(original_user_dictionary)
        return original_user_dictionary
