age = int(input("How old are you? \n"))
#input is inside int function to get whole number

decades = age // 10
#// is to divde whole number

years = age % 10 
#modulus to get remainder

print("You are " + str(decades) + " decades and " + str(years) + " year(s) old.")
#put the decades/years vars back into string format to print for conacetation. 
