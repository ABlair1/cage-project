from imdb import IMDb

# Create an instance of the IMDb class
ia = IMDb()

# Get info for Nic Cage
nic = ia.get_person('0000115')

# # Get info for each Nic Cage movie
for movie in nic['filmography']['actor']:
    # Get IMDb movie ID
    id = movie.movieID

    # Retrieve movie data 
    current = ia.get_movie(id)
    ia.update(current, info=['main', 'plot', 'vote details'])
    cast_i = 0
    while str(current['cast'][cast_i]) != 'Nicolas Cage':
        cast_i += 1

    title = str(current['title'])
    year = str(current.get('year', 'TBA'))
    role = str(current['cast'][cast_i].currentRole)
    coverURL = current.get('cover url', 'TBA')
    plot = current.get('plot', 'TBA')
    runtime = current.get('runtimes', 'TBA')
    imdb_rating = str(current.get('arithmetic mean', 'None'))

    # Adjust runtime based on current being a movie or series
    if runtime != 'TBA':
        if 'movie' in str(current['kind']).lower():
            runtime = runtime[0] + ' minutes'
        else:
            runtime = 'Varies by episode'

    # Get first plot description from plot list
    if plot != 'TBA':
        plot = str(plot[0])

    print("id: ", id, ", title: ", title, ", year: ", year, ", runtime: ", runtime, 
        ", role: ", role, "imdb_rating: ", imdb_rating)
    print("coverURL: ", coverURL)
    print("plot: ", plot)
