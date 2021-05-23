def dictionary2():
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)
    Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
    print("\nDictionary with the use of dict(): ")
    print(Dict)
    Dict = dict([(1, 'Geeks'), (2, 'For')])
    print("\nDictionary with each item as a pair: ")
    print(Dict)


def dictionary3():
    Dict = {1:1,  3: 3}
    print("Empty Dictionary: ")
    print(Dict)

    # Adding elements one at a time
    Dict[0] = 'Geeks'
    Dict[2] = 'For'

    #Dict[3] = 1
    print("\nDictionary after adding 3 elements: ")
    print(Dict)
    #{1:1 , 0: 'Geeks', 2: 'For', 3: 1}

    # Adding set of values
    # to a single Key
    Dict['Value_set'] = 2, 3, 4
    print("\nDictionary after adding 3 elements: ")
    print(Dict)

    # Updating existing Key's Value
    Dict[2] = 'Welcome'
    print("\nUpdated key value: ")
    print(Dict)

    # Adding Nested Key value to Dictionary
    Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks', 1:1}}
    print("\nAdding a Nested Key: ")
    print(Dict)
    #{0: 'Geeks', 2: 'Welcome', 3: 1, 5:{'Nested' :{'1' : 'Life',1:1, '2' : 'Geeks'}}}
    print(Dict[5]['Nested']['2'])

    # del Dict[1]
    # del Dict[3]
    # del Dict[0]
    # del Dict[2]
    # del Dict['Value_set']

    print(Dict[5].pop('Nested'))
    print(Dict)

#GIT
#practice on the dictionaries, tweets- loops to print out values
#utilise dictionaries
#use the twitter link and practice using the activities i've done

