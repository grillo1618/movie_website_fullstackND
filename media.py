"""
    This file defines a module that contains the classes that will model
    the data structure for the entertainment center, that will also be used
    to display the data through the movie_trailer_site.py methods.
"""
import webbrowser


class Video(object):
    """This class represents a video data structure."""

    def __init__(self, v_title, v_duration=0.0):
        """This method initializes the initial stage of a video object."""
        self.title = str(v_title)
        self.duration = v_duration

    def show_info(self):
        """This method shows the information of the a video."""
        print("Video Title: " + self.title)
        print("Video Duration: " + str(self.duration))

    def get_title(self):
        """Returns the title o the video."""
        return self.title

    def get_duration(self):
        """Returns the duration of the video."""
        return self.duration

    def set_title(self, v_title=""):
        """Sets the title of the video."""
        if isinstance(str(v_title), str):
            self.title = str(v_title)
            return True
        else:
            print("Argument Error: The title argument passed is not a string.")
            return False

    def set_duration(self, duration=0.00):
        """Sets the duration of the video."""
        if isinstance(float(duration), float):
            self.duration = duration
            return True
        else:
            print("Argument Error: The duration argument passed " +
                  "is not of a number.")
            return False

    def class_info(self):
        """Prints the information of the class with predefined variables."""
        print("=======================================================" +
              "================================================")
        print("Class Name: " + Video.__name__)
        print("--------------------------------------------------------" +
              "-----------------------------------------------")
        print("Doc Description: " + Video.__doc__)
        print("----------------------------------------------------------" +
              "---------------------------------------------")
        print("Inherits From: " + str(Video.__bases__))
        print("--------------------------------------------------------" +
              "-----------------------------------------------")
        print("Loaded From: " + Video.__module__ + ".py")
        print("---------------------------------------------------------" +
              "----------------------------------------------")
        print("Current Namespace: " + str(Video.__dict__))
        print("=========================================================" +
              "==============================================")

        class_info_data = (Video.__name__, Video.__doc__, Video.__bases__,
                           Video.__module__, Video.__dict__)
        return class_info_data


class Movie(Video):
    """This class represents a movie data structure."""

    # Class Variables:
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, storyline, poster_image_url,
                 trailer_youtube_url, rating="NA"):
        """Initializes an instance of the class Movie."""
        super(Movie, self).__init__(title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

        # Verifies rating validity and assigns if valid, if not, assign NA.
        if str(rating).upper() in Movie.VALID_RATINGS:
            self.rating = rating
        else:
            self.rating = "NA"

    def show_trailer(self):
        """This function shows the trailer of the movie
        (calling show_trailer).
        """
        webbrowser.open(self.trailer_youtube_url)

    def get_ratings(self):
        """Gets the rating of the movie."""
        return self.rating

    def get_storyline(self):
        """Return the storyline of the movie."""
        return self.storyline

    def get_poster_img_url(self):
        """Return the video poster imgage's url."""
        return self.poster_image_url

    def get_trailer_youtube_url(self):
        """Return the youtube video url from the movie."""
        return self.trailer_youtube_url

    def set_trailer_youtube_url(self, trailer_url=""):
        """Sets the movie's youtube movie trailer url."""
        if str(trailer_url) != "":
            self.trailer_youtube_url = trailer_url
        else:
            print("Argument Error: The url for the movie trailer is " +
                  "not valid.")

    def set_storyline(self, storyline=""):
        """Sets the movie's storyline text."""
        if str(storyline) != "":
            self.storyline = storyline
        else:
            print("Argument Error: The storyline for the movie's " +
                  "storyline is not valid.")

    def set_poster_img_url(self, poster_url=""):
        """Sets the movie poster's url."""
        # Could be awesome to have regex for this validation.
        if str(poster_url) != "":
            self.poster_image_url = poster_url
        else:
            print("Argument Error: The storyline for the movie's " +
                  "storyline is not valid.")

    def class_info(self):
        """Prints the information of the class with predefined variables."""
        print("=======================================================" +
              "================================================")
        print("Class Name: " + Movie.__name__)
        print("--------------------------------------------------" +
              "-----------------------------------------------------")
        print("Doc Description: " + Movie.__doc__)
        print("--------------------------------------------------" +
              "-----------------------------------------------------")
        print("Inherits From: " + str(Movie.__bases__))
        print("--------------------------------------------------" +
              "-----------------------------------------------------")
        print("Loaded From: " + Movie.__module__ + ".py")
        print("-----------------------------------------------------" +
              "--------------------------------------------------")
        print("Current Namespace: " + str(Movie.__dict__))
        print("=====================================================" +
              "==================================================")

        class_info_data = (Movie.__name__, Movie.__doc__, Movie.__bases__,
                           Movie.__module__, Movie.__dict__)
        return class_info_data


class MovieLibrary(object):
    """This class represents a library of movies.
    SPECIAL NOTE: THIS CLASS WILL BE EXTENDED."""

    def __init__(self, movie_library=[]):
        """This method initializes a movie library."""
        if isinstance(movie_library, list):
            self._library = movie_library
        else:
            self._library = []

    def get_library(self):
        """This method returns the library's movie content."""
        return self._library

    def set_library(self, movie_library):
        """This method sets a whole array as the library of movies, awesome!"""
        if isinstance(movie_library, list):
            if len(movie_library) > 0:
                self._library = movie_library
        else:
            print("Argument Error: The movie library " +
                  "argument is not a valid list.")

    def insert_mov(self, movie):
        """This method inserts a movie into the library."""
        # Check first if the movie parameter is an instance
        # of Movie, else throw an argument exception.
        if isinstance(movie, Movie):
            self._library.append(movie)
        else:
            print("Argument Error: The argument is " +
                  " not an instance of Movie class.")

    def remove_mov(self, movie):
        """This method removes a movie in the library equal to the movie."""
        if isinstance(movie, Movie):
            if movie in self._library:
                index_of_item = self._library.index(movie)
                self._library.pop(index_of_item)
        else:
            print("Argument Error: The movie argument is not a valid Movie.")


# class TvShow(Video):
#     """This class represents a TvShow."""
#
#     def __init__(self, title, duration, season, episode, tv_station):
#         """Initializes an instance of the class TvShow."""
#         super().__init__(str(title), duration)
#         self.season = season
#         self.episode = episode
#         self.tv_station = tv_station
#
#     def get_local_listing(self):
#         """What is this?"""
#         return False
