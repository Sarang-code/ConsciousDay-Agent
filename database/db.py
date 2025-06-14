import sqlite3 #  Imports Python’s built-in sqlite3 library

# function to create database and its table (if it doesn't already exist).
def create_db(): 
    conn = sqlite3.connect("entries.db") # Connects to the SQLite database file named entries.db. If it doesn’t exist, SQLite will automatically create it
    cursor = conn.cursor() # Creates a object which allows you to execute SQL commands.

    # SQL query to create a table
    cursor.execute("""CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        journal TEXT,
        intention TEXT,
        dream TEXT,
        priorities TEXT,
        reflection TEXT,
        strategy TEXT
    )""")
    conn.commit() #  Saves (commits) the changes to the database file.
    conn.close() # Closes the database connection to free up system resources

# Function to insert a new row into the entries table using a dictionary data.
def save_entry(data):
    conn = sqlite3.connect("entries.db")
    cursor = conn.cursor()

    # Inserts the values from the data dictionary into the corresponding database columns.
    cursor.execute("INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (data["date"], data["journal"], data["intention"], data["dream"], data["priorities"], data["reflection"], data["strategy"]))
    conn.commit()
    conn.close()

#  Defines a function to fetch all entries that match a given date.
def get_entries_by_date(date):
    conn = sqlite3.connect("entries.db")
    cursor = conn.cursor()

    # Selects all rows from the entries table where the date matches the provided value.
    cursor.execute("SELECT * FROM entries WHERE date = ?", (date,))
    result = cursor.fetchall() # Fetches all matching rows from the result of the SQL query
    conn.close()
    return result # returns the list of matching entries.
