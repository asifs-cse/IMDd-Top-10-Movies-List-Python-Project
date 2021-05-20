# first install IMDB library
import imdb
ib = imdb.IMDb()

search = ib.get_top250_movies()

for i in range(1, 10+1):
    print(f"Number: {i} {search[i]}")

# finish code
