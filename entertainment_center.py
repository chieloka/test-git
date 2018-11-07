import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")
school_of_rock = media.Movie("School of Rock",
                        "A rock story",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "http://www.youtube.com/watch?v=3PsUJFEBC74")

#print(toy_story.storyline)

#toy_story.show_trailer()

print(media.Movie.VALID_RATINGS)

movie_list = [toy_story,school_of_rock]

fresh_tomatoes.open_movies_page(movie_list)
