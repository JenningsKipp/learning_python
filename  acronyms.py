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

#######################################

#Check if Exists in List
word = 'Yeehaw'

if word in acronyms:
    print(word + ' is in the list.')
else:
    print(word + ' is not in the list.')
    
#expected result: Yeehaw is not in the list.

#######################################

#want to print each acronym in the list on a separate line? Make a loop!
#for loop, for describes the loop- acronym1 is the loop variable- acronym2 is the list we're looping through.
for acronym in acronyms:
    print(acronym)