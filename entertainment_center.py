#!/usr/bin/env python
# encoding: utf-8

from media import Movie
from fresh_tomatoes import open_movies_page

idenity = Movie(
    "Identity",
    "http://goo.gl/K4HIeh",
    "https://www.youtube.com/watch?v=S8fjyxM7DgU",
    "2003"
)

the_prestige = Movie(
    "The Prestige",
    "http://goo.gl/Bj06fy",
    "https://www.youtube.com/watch?v=o4gHCmTQDVI",
    "2006"
)

ratatouille = Movie(
    "Ratatouille",
    "http://goo.gl/r5yOz6",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
    "2007"
)

movies = [idenity, the_prestige, ratatouille]
open_movies_page(movies)



