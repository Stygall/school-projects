dictionary = {'users':{'dave': {'score': 0 }}}
for var in dictionary['users'].keys():
    if var == 'dave':
        for item in dictionary[var].keys():
            if item == 'score':
                print(item)