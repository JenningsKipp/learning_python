#A Dictionary Maps Keys to Values

acronyms = {
    'LOL' : 'laugh out loud',
    'IDK' : "I don't know",
    'TBH' : 'to be honest'
}
print(acronyms)

#Update Value
acronyms['TBH'] = 'to be hangry'

#To look up an item in a dictionary we send in the key in square brackets
print(acronyms['LOL'])

#Dictionaries can hold anything
#ex: Strings to strings like above
#ex: strings to numbers menu = {'Soup : 5, 'Salad' : 6}
#ex: anything my_dict = {10: 'hello', 2: 6.5}

#to create a dictionary name it and empty curly brackets
albums = {}
#Adding syntax almost looks like looking them up
albums['Songs in the Key of Life'] = 'Stevie Wonder'
albums['Nothing Was The Same'] = 'Drake'
albums['Rumours'] = 'Fleetwood Mac'

print(albums)

#Acessing a key that doesn't exist will result in key error.
#definition = acronyms['BTW']

#To avoid this use the .get method, it won't crash your program and will return none type
definition = acronyms.get('BTW')
print(acronyms)

if definition:
    print(definition)
else:
    print("Key doesn't exist")
    
sentence = 'IDK' + ' I hate ' + 'TBH'
translation = acronyms.get('IDK') + ' I hate ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)