# Sarah Ma
# Lab 6 - Dictionaries, Sets, and APIs

# TMDB import and API key
import tmdbsimple as tmdb
tmdb.API_KEY = ''

def main(): 
	# Takes input from the user of what name of the movie they want to search up 
	search_movie = input('Enter the name of the movie you want to search: ')

	# This part was given from the sample code from github 
	# I just changed the query=f'{search_movie}' which essentially searches up the movie the user enters
	search = tmdb.Search()
	response = search.movie(query=f'{search_movie}')

	# This part wasn't requested in the lab but I did it anyway
	# This checks if the movie the user enters is found in the database and if it's not then it allows the user to enter in a movie that exists
	while not search.results:
		print(f'The movie {search_movie} does not exist in the database.')
		search_movie = input('Enter the name of the movie you want to search: ')
		search = tmdb.Search()
		response = search.movie(query=f'{search_movie}')

	# If the movie is found in the database then it iterates through each movie with that name and prints out the name, id, popularity, and release date of the movie
	for movie in search.results:
		print(movie['title'], movie['id'], movie['popularity'], movie['release_date'])

		# Opens a csv file to write to
		file_write = open('movie_results.csv', 'w')
		# Prints the headers of the columns for clarity
		file_write.write('Name,ID,Popularity,ReleaseDate\n')
		# Same loop as when the results were printed but instead writes it to the csv file
		for movie in search.results:
			file_write.write(f"{movie['title']},{movie['id']},{movie['popularity']},{movie['release_date']}\n")
			
		# Close file to save everything
		file_write.close()

main()
