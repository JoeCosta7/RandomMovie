import sqlite3
import pandas as pd
import random

def access():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movie ORDER BY ROWID ASC LIMIT 1")
    row = cursor.fetchone()
    columns = [column[0] for column in cursor.description]
    movie_dict = dict(zip(columns, row))
    filtered_dict = {key: value for index, (key, value) in enumerate(movie_dict.items()) if 1 <= index <= 5 and value == 1}
    
    df = pd.DataFrame(columns=["title","type","genres","releaseYear","imdbId","imdbAverageRating","imdbNumVotes", "availableCountries"])
    for key in filtered_dict.keys():
        temp_df = pd.read_csv(f"movie/data/{key}.csv")
        temp_df.dropna(inplace=True)
        df = pd.concat([df, temp_df], ignore_index=True)
    values = list(movie_dict.values())
    min_rating = values[6]
    max_rating = values[7]
    min_year = values[8]
    max_year = values[9]
    genre = values[10]
    filtered_df = df.query(f"imdbAverageRating >= {min_rating} and imdbAverageRating <= {max_rating} and releaseYear >= {min_year} and releaseYear <= {max_year} and genres.str.contains('{genre}') and availableCountries.str.contains('US') and type == 'movie'")
    random_movies = filtered_df['title'].tolist()
    random_movie = random.choice(random_movies)
    conn.close()
    return random_movie

