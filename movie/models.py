from flask import g
import sqlite3

def get_db():
    """Connect to database and return connection"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db.sqlite3')
        db.row_factory = sqlite3.Row
    return db

def create_movie_table():
    """Create movie table"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, max INTEGER NOT NULL CHECK (max IN (0, 1)), netflix INTEGER NOT NULL CHECK (netflix IN (0, 1)), hulu INTEGER NOT NULL CHECK (hulu IN (0, 1)), prime INTEGER NOT NULL CHECK (prime IN (0, 1)), appletv INTEGER NOT NULL CHECK (appletv IN (0, 1)), min_rating REAL, max_rating REAL, min_year INTEGER, max_year INTEGER, genre TEXT)''')
    db.commit()

def add_movie(max, netflix, hulu, prime, appletv, min_rating, max_rating, min_year, max_year, genre):
    """Add movie to database"""
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''INSERT INTO movie (max, netflix, hulu, prime, appletv, min_rating, max_rating, min_year, max_year, genre) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (max, netflix, hulu, prime, appletv, min_rating, max_rating, min_year, max_year, genre))
        db.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

def get_movies():
    """Get movies from database"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM movie''')
    return cursor.fetchall()