import fresh_tomatoes
import media

toy_stroy = media.Movie("Toy Story",
                       "A Story of a boy",
                       "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                       "https://www.youtube.com/watch?v=SgoiKLFBA3Q")

# print (toy_stroy.storyline);

avatar_story = media.Movie("Avatar",
                       "Avatar",
                       "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                       "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# avatar_story.show_trailer();
movies = [toy_stroy,avatar_story]
# fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATING)
print (media.Movie.__doc__)