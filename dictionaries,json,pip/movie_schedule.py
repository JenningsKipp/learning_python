
current_movies = {'Pulp Fiction': '12:00pm',
                  'Curious George': '12:45pm',
                  'Home Alone 6: How Does This Keep Happening?' :'4:35pm'}

print("We're showing the follwing movies:")
for key in current_movies:
    print(key)


movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime is None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)