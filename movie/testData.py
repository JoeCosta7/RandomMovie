import sqlite3

def view_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')  
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM movie') 
    rows = cursor.fetchall()

    # Check if there are any rows and print them
    if rows:
        print("Data in the 'movie' table:")
        for row in rows:
            print(row)  
    else:
        print("No data found in the table.")

    # Close the connection
    conn.close()

# Call the function to view data
view_data()