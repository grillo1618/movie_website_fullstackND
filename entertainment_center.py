"""This file actually constructs the movie_trailer_site website."""

from media import Movie, MovieLibrary
import movie_trailer_site

beautiful_mind = Movie("A Beautiful Mind",
                       135,
                       "After John Nash, a brilliant but " +
                       "asocial mathematician, accepts secret work in " +
                       "cryptography, his life takes a turn for the " +
                       "nightmarish.",
                       "https://images-na.ssl-images-amazon.com/images/" +
                       "M/MV5BMzcwYWFkYzktZjAzNC00OGY1LWI4YTgtNzc5MzVjM" +
                       "DVmNjY0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_" +
                       "CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=0UgO3XGO6Ag",
                       "PG-13")

goethe_in_love = Movie("Young Goethe In Love",
                       102,
                       "After aspiring poet Johann Wolfgang von Goethe " +
                       "fails his law exams, he's sent to a sleepy " +
                       "provincial court to reform. Instead, he falls " +
                       "for Lotte, a young woman who is promised " +
                       "to another man.",
                       "https://upload.wikimedia.org/wikipedia/en" +
                       "/thumb/8/8a/YoungGoetheInLove2010Poster.jpg" +
                       "/220px-YoungGoetheInLove2010Poster.jpg",
                       "https://www.youtube.com/watch?v=IqLvKhL2HbQ")

casper = Movie("Casper",
               100,
               "A paranormal expert and his daughter bunk in an abandoned " +
               "house populated by three mischievous ghosts and one " +
               "friendly one.",
               "https://images-na.ssl-images-amazon.com/" +
               "images/M/MV5BZThhYTlhMDUtMDhjZi00MTlj" +
               "LTkwMDYtOGU3ZjVlMWE4NDk4XkEyXkFqcGdeQXVyMTQxNzMzNDI@." +
               "_V1_UY268_CR5,0,182,268_AL_.jpg",
               "https://www.youtube.com/watch?v=6ayULcBzbkM",
               "PG")

star_wars_i = Movie("Star Wars: Episode I: The Phantom Menace",
                    136,
                    "Two Jedi Knights escape a hostile blockade to find " +
                    "allies and come across a young boy who may bring " +
                    "balance to the Force, but the long dormant Sith " +
                    "resurface to claim their old glory.",
                    "https://images-na.ssl-images-amazon.com/images/M/" +
                    "MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNW" +
                    "I0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182" +
                    "_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=bD7bpG-zDJQ",
                    "PG")

star_wars_ii = Movie("Star Wars: Episode II - Attack of The Clones",
                     144,
                     "Ten years after initially meeting, Anakin Skywalker " +
                     "shares a forbidden romance with Padme, while Obi-Wan " +
                     "investigates an assassination attempt on the " +
                     "Senator and discovers a secret clone army " +
                     "crafted for the Jedi.",
                     "https://images-na.ssl-images-amazon.com/images/M/" +
                     "MV5BOWNkZmVjODAtNTFlYy00NTQwLWJhY2UtMmFmZTkyOWJmZjZ" +
                     "iL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._" +
                     "V1_UY268_CR10,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=gYbW1F_c9eM",
                     "PG")

star_wars_iii = Movie("Star Wars: Episode III - Revenge of the Sith",
                      140,
                      "Three years into the Clone Wars, the Jedi rescue " +
                      "Palpatine from Count Dooku. As Obi-Wan pursues " +
                      "a new threat, Anakin acts as a double agent between " +
                      "the Jedi Council and Palpatine and is lured into a " +
                      "sinister plan to rule the galaxy.Three years " +
                      "into the Clone Wars, the Jedi rescue Palpatine " +
                      "from Count Dooku. As Obi-Wan pursues a new threat, " +
                      "Anakin acts as a double agent between the " +
                      "Jedi Council and Palpatine and is lured into a " +
                      "sinister plan to rule the galaxy.",
                      "https://images-na.ssl-images-amazon.com/images/M/" +
                      "MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@" +
                      "._V1_UY268_CR9,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=5UnjrG_N8hU",
                      "PG-13")

star_wars_iv = Movie("Star Wars: Episode IV - A New Hope",
                     121,
                     "Luke Skywalker joins forces with a Jedi Knight, a" +
                     " cocky pilot, a Wookiee and two droids to save the " +
                     "galaxy from the Empire's world-destroying battle-" +
                     "station while also attempting to rescue Princess " +
                     "Leia from the evil Darth Vader.",
                     "https://images-na.ssl-images-amazon.com/images/M/" +
                     "MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1" +
                     "ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_" +
                     "CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=9gvqpFbRKtQ",
                     "PG")

star_wars_v = Movie("Star Wars: Episode V - The Empire Strikes Back",
                    124,
                    "After the rebels are overpowered by the Empire on"
                    " their newly established base, Luke Skywalker begins "
                    "Jedi training with Yoda. His friends accept shelter "
                    "from a questionable ally as Darth Vader hunts them "
                    "in a plan to capture Luke.",
                    "https://images-na.ssl-images-amazon.com/images/M/" +
                    "MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OT" +
                    "E0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_" +
                    "UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                    "PG")

star_wars_vi = Movie("Star Wars: Episode VI - Return of the Jedi",
                     131,
                     "After a daring mission to rescue Han Solo from Jabba " +
                     "the Hutt, the rebels dispatch to Endor to destroy " +
                     "a more powerful Death Star. Meanwhile, Luke " +
                     "struggles to help Vader back from the dark side " +
                     "without falling into the Emperor's trap.",
                     "https://images-na.ssl-images-amazon.com/images/M/" +
                     "MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1" +
                     "XkEyXkFqcGdeQXVyNTAyODkwOQ@@._" +
                     "V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=5UfA_aKBGMc",
                     "PG")

castle_in_the_sky = Movie("Castle in the Sky",
                          125,
                          "A young boy and a girl with a magic crystal must" +
                          " race against pirates and foreign agents in a " +
                          "search for a legendary floating castle.",
                          "https://images-na.ssl-images-amazon.com/images/" +
                          "M/MV5BNTg0NmI1ZGQtZTUxNC00NTgxLThjMDUtZmRlYmEz" +
                          "M2MwOWYwXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._" +
                          "V1_UY268_CR2,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=McM0_YHDm5A",
                          "PG")

lord_of_the_rings_i = Movie("The Lord of the Rings: The Fellowship of the " +
                            "Ring",
                            178,
                            "A meek Hobbit from the Shire and eight " +
                            "companions set out on a journey to destroy " +
                            "the powerful One Ring and save Middle Earth " +
                            "from the Dark Lord Sauron.",
                            "https://images-na.ssl-images-amazon.com/images/" +
                            "M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2Vl" +
                            "OTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1" +
                            "_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=aStYWD25fAQ",
                            "PG-13")

lord_of_the_rings_ii = Movie("The Lord of the Rings: The Two Towers",
                             179,
                             "While Frodo and Sam edge closer to Mordor " +
                             "with the help of the shifty Gollum, the " +
                             "divided fellowship makes a stand against " +
                             "Sauron's new ally, Saruman, and his" +
                             " hordes of Isengard.",
                             "https://images-na.ssl-images-amazon.com/" +
                             "images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExLTky" +
                             "ZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVyNjU0" +
                             "OTQ0OTY@._V1_UY268_CR1,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=LbfMDwc4azU",
                             "PG-13")

lord_of_the_rings_iii = Movie("The Lord of the Rings: The Return of the King",
                              201,
                              "Gandalf and Aragorn lead the World of Men "
                              "against Sauron's army to draw his gaze from"
                              " Frodo and Sam as they approach Mount Doom "
                              "with the One Ring.",
                              "https://images-na.ssl-images-amazon.com/" +
                              "images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLW" +
                              "E1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyN" +
                              "DUyOTg3Njg@._V1_UX182_CR0,0,182,268_AL_.jpg",
                              "https://www.youtube.com/watch?v=y2rYRu8UW8M",
                              "PG-13")

the_matrix = Movie("The Matrix",
                   136,
                   "A computer hacker learns from mysterious rebels about"
                   " the true nature of his reality and his role in the"
                   " war against its controllers.",
                   "https://images-na.ssl-images-amazon.com/images" +
                   "/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNk" +
                   "YzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@." +
                   "_V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://www.youtube.com/watch?v=Q8g9zL-JL8E",
                   "R")

movies = [beautiful_mind, goethe_in_love, casper, star_wars_i, star_wars_ii,
          star_wars_iii, star_wars_iv, star_wars_v, star_wars_vi,
          castle_in_the_sky, lord_of_the_rings_i, lord_of_the_rings_ii,
          lord_of_the_rings_iii]
movie_library = MovieLibrary(movies)

movie_trailer_site.open_movies_page(movie_library.get_library())
