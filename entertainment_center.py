import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://images-na.ssl-images-amazon.com/images/I/91g2fEXursL._RI_SX200_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

inception = media.Movie("Inception",
                        "The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for the implantation of another person's idea into a target's subconscious",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://youtu.be/8hP9D6kZseM")


movies = [toy_story,inception]
fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline)
#inception.show_trailer()
