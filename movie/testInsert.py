import sqlite3

def insert_data():
    conn = sqlite3.connect('db.sqlite3')  # Connect to the database
    cursor = conn.cursor()
    
    # Insert data into the table
    cursor.execute('''
        INSERT INTO movie (max, netflix, hulu, prime, appletv, min_rating, max_rating, min_year, max_year, genre) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (1, 1, 1, 1, 1, 4.0, 7.0, 1900, 2025, "Action"))  # Example data

    conn.commit()  # Commit the transaction to save changes
    conn.close()   # Close the connection

insert_data()