temperature = int(input("What's the degrees outside?\n"))
forecast =  "sunny"

if temperature < 80 and forecast != "rainy" :
    print("Go Outside!")
else:
    print("Stay indoors!")