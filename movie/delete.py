import sqlite3

def insert_data():
    conn = sqlite3.connect('db.sqlite3')  # Connect to the database
    cursor = conn.cursor()
    
    # Insert data into the table
    
    cursor.execute('DELETE FROM movie')
        

    conn.commit()  # Commit the transaction to save changes
    conn.close()   # Close the connection

insert_data()