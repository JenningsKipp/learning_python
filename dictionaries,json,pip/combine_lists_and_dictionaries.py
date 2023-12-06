#three separate menu lists: breakfast, lunch, and dinner

breakfast = ['Eggs benedict', 'French Toast', 'Orange Juice']

lunch = ['Sushi', 'BLT', 'Grilled Cheese']

dinner = ['Gumbo', 'Ramen', 'Chicken & Dumplings']

#we would like to combine these lists, in python you can have a container of containers. or a list of lists, see below

# menus = [ ['Eggs benedict', 'French Toast', 'Orange Juice'], ['Sushi', 'BLT', 'Grilled Cheese'],
# ['Gumbo', 'Ramen', 'Chicken & Dumplings']]

#you can print each list by using bracket notation with their positions 0,1,2

# print('Breakfast Menu:\t', menus[0]) #first list
# print('Lunch Menu:\t', menus[1]) #second list
# print('Dinner Menu:\t', menus[2]) #third list

#how would we get an item inside of an individual list? 2 indexes can be used
# print(menus[0])
# print(menus[0][1])

#instead of using a list within a listh thou we can use a dictionary. it just looks better 
menus = { 'Breakfast' : ['Eggs benedict', 'French Toast', 'Orange Juice'],
        'Lunch' : ['Sushi', 'BLT', 'Grilled Cheese'],
        'Dinner' : ['Gumbo', 'Ramen', 'Chicken & Dumplings']
}

#for loop over a dictionary so we dont have to print individual lists
for name, menu in  menus.items():
    print(name, ':', menu)
    
#Dictionaries can be used to represent objects
person = { 'name': 'Kipp Jennings',
          'city' : 'Auburn',
          'age' : '31'}

print(person.get('name'), 'is', person.get('age'), 'year(s) old.')