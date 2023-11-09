acronyms = ['OMG', 'TTYL', 'SMH']

acronyms.append('LOL')
acronyms.append('IDK')

print(acronyms)

#acronyms is the list
#methods are called on objects
#.append is the method name
#what you want to add is in parentheses

#to remove you can use the remove method see below
acronyms.remove('LOL')
print(acronyms)
#or remove item by specified index using del
del acronyms[0]
print(acronyms)
