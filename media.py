import webbrowser   # webbrowser module so we can launch trailer videos


class Media():
    """ This class provides a way to store media related information. """
    def __init__(self, title, description, image, youtube, genre):
        self.title = title
        self.description = description
        self.image_url = image
        self.youtube_url = youtube
        self.genre = genre

    def show_video(self):
        webbrowser.open(self.youtube_url)


class Movie(Media):
    """ This class inherits from Media and provides a way to store movie related
     information. """
    def __init__(self, title, description, image, youtube, genre, rating, year,
                 director):
        Media.__init__(self, title, description, image, youtube, genre)
        self.rating = rating
        self.year = year
        self.director = director


class TVshow(Media):
    """ This class inherits from Media and provides a way to store TV show
    related information. """
    def __init__(self, title, description, image, youtube, genre, seasons,
                 episodes, episode_length):
        Media.__init__(self, title, description, image, youtube, genre)
        self.seasons = seasons
        self.episodes = episodes
        self.episode_length = episode_length
