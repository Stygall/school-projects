dictionary = {'user' : ['user@user.nl', 'ik ben user', {'score': 6125, 'codes': ['12hjb2', 'jk123']}]}
user = input('give a username: ')
if user in dictionary.keys():
    print (dictionary[user])
    quiz = 'jan2020'
    user_dict = dictionary[user][2]
    if quiz in quiz_dict.keys():
        print(quiz_dict[quiz])