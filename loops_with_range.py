# for i in range(7):
#     print(i)
# #expect 0-6

# total = 0
# expenses = []

# for i in range(7):
#     expenses.append(float(input("Enter an expense:")))
    
# total = sum(expenses)

# print("You spent $", total, sep=' ')

#Want to give the user the option to add the amount of expenses they have?

total = 0 
expenses = []

num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))
    
total = sum(expenses)
print("You spent $", total, sep = ' ')