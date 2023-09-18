class Movie:
    """Create a Movie object from the title, genre, director, and year passed in."""

    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def __repr__(self):
        return f"{self._title} ({self._year})"

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year


class StreamingService:
    """Create a Streaming Service object from a series of Movie objects"""

    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def __repr__(self):
        return f"{self._name} has {len(self._catalog)} movies"

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie):
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, movie_title):
        if movie_title in self._catalog:
            del self._catalog[movie_title]


class StreamingGuide:
    """Create a Streaming Guide with a series of Streaming Service objects"""

    def __init__(self):
        self._services = []

    def __repr__(self):
        return f"There are {len(self._services)} streaming services"

    def add_streaming_service(self, streaming_service):
        self._services.append(streaming_service)

    def delete_streaming_service(self, name):
        for service in self._services:
            if service.get_name() == name:
                index = self._services.index(service)
        self._services.pop(index)

    def where_to_watch_movie(self, movie_title):
        places = []
        for service in self._services:
            catalog = service.get_catalog()
            if movie_title in catalog:
                movie = catalog[movie_title]
                year = movie.get_year()
                if len(places) == 0:
                    places.append(f"{movie_title} ({year})")
                places.append(service.get_name())
        if len(places) == 0:
            return None
        return places


movie_1 = Movie("The Seventh Seal", "comedy", "Ingmar Bergman", 1957)
movie_2 = Movie("Home Alone", "tragedy", "Chris Columbus", 1990)
movie_3 = Movie("Little Women", "action thriller", "Greta Gerwig", 2019)
movie_4 = Movie("Galaxy Quest", "historical documents", "Dean Parisot", 1999)

stream_serv_1 = StreamingService("Netflick")
stream_serv_1.add_movie(movie_2)


stream_serv_2 = StreamingService("Hula")
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie("The Seventh Seal")
stream_serv_2.add_movie(movie_2)


stream_serv_3 = StreamingService("Dizzy+")
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)


stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service("Hula")
search_results = stream_guide.where_to_watch_movie("Little Women")
print(search_results)
