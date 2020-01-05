import pickle


def pickleAFile(reason, dumpDict):
    filename = reason + '_pickle.txt'
    with open(filename, 'wb') as file:
        pickle.dump(dumpDict, file)
        file.close()


reason = input()
choice = input()

if choice == '1':
    dumpDict = {'Miel': ['Miel', 'mielisawesome', ['nl_en', 'en_nl']], 'Dev': ['Dev', 'test123']}
    print (dumpDict)
    pickleAFile(reason, dumpDict)
elif choice == '2' :
    dumpDict = {'brood':[5,'brood','bread'],
'zelfmoord':[5,'zelfmoord','suicide'],
'broodrooster':[5,'broodrooster','toaster'],
'badkuip':[5,'badkuip','bathtub'],
'pindakaas':[5,'pindakaas','peanutbutter'],
'jam':[5,'jam','jelly'],
'augurk':[5,'augurk','pickle'],
'handtas':[5,'handtas','purse'],
'voordeur':[5,'voordeur','front door'],
'kestboom':[5,'kerstboom','christmas tree']
}

    pickleAFile(reason,dumpDict)