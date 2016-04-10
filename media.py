#!/usr/bin/env python
# encoding: utf-8

class Movie:
    """
    This is a class for movie information

    Attributes:
        title (str): The title of the movie
        poster_image_url (str): The url of the movie poster
        trailer_youtube_url (str): The url of the movie trailer in Youtube
        relese_date (str): The year when the movie is released
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url, release_date):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date

