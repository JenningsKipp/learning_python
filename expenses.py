#list of expenses everytime we went out to eat
# expenses = [10.50, 8, 7, 45, 3, 3.5]
# #start with a sum of zero
# sum = 0 
# #for every exepense(x) in expenses, take sum and add each expense.
# for x in expenses:
#     sum = sum + x
# #print out how much you spent. Sep is used here to remove the blank space provided from the comma in our print statement.
# #Try removing sep(and the comma after sum) to see the difference in the print statement.
# print('You spent $', sum, sep = '')

#BUT PYTHON HAS A SUM FOR LISTS FUNCTION

individual_costs = [4, 7, 8, 10.50, 19, 20, 10]
#sum function receiving our list and assigning that to a variable of total
sum = sum(individual_costs)

print('You spent $', sum, sep = '')