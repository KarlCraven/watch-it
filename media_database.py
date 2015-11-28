import media        # media module holds Media, Movie, and TVshow classes
import watch_it     # amended version of Fresh Tomatoes module
import csv          # module for working with csv files

# we start with an empty array to add our media objects to
media_list = []

# access csv file containing media object data
with open('media.csv', 'r') as data:
    reader = csv.reader(data)

    # use the data from each row to instantiate either a Movie or TVshow object
    for row in reader:

        # the second cell in each row is used to decide if a Movie or TVshow
        # object needs to be created
        if row[1] == "Movie":
            media_list.append(media.Movie(row[0], row[2], row[3], row[4],
                                          row[5], row[6], row[7], row[8]))
        elif row[1] == "TV Show":
            media_list.append(media.TVshow(row[0], row[2], row[3], row[4],
                                           row[5], row[9], row[10], row[11]))

# we're done with the csv file, so we close it
data.close()

# generate our webpage by calling a function from the watch_it module and
# passing it our populated array of objects
watch_it.open_media_page(media_list)
