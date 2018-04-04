import media
import fresh_tomatoes

fight_club = media.Movie("Fight Club",
                        "A story about fighting and soap.",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://youtu.be/J8FRBYOFu2w")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Dances with wolves with aliens",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

the_usual_suspects = media.Movie("The Usual Suspects",
                                 "neo-noir mystery film whodunnit",
                                 "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
                                 "https://youtu.be/oiXdPolca5w")

#the_usual_suspects.show_trailer()

the_godfather_part_II = media.Movie("The Godfather Part II",
                                    "A timeless tale about the Corleone family",
                                    "https://upload.wikimedia.org/wikipedia/en/0/03/Godfather_part_ii.jpg",
                                    "https://youtu.be/qJr92K_hKl0")

interstellar = media.Movie("Interstellar",
                           "Searching for home after earth",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://youtu.be/zSWdZVtXT7E")


the_prestige = media.Movie("The Prestige",
                           "Competitive magicians may have taken it too far",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                           "https://youtu.be/o4gHCmTQDVI")

movies = [fight_club, avatar, the_usual_suspects, the_godfather_part_II, interstellar, the_prestige]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)
