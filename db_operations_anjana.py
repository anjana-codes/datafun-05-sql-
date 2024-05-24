import sqlite3
import csv

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create authors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
)
''')

# Open the CSV file and read its content
with open('authors.csv', 'r') as data:
    reader = csv.reader(data)
    next(reader)  # Skip the header row
    authors_data = [row for row in reader]

    
# Insert data into authors table
cursor.executemany('''
INSERT OR IGNORE INTO authors (author_id, first, last)
VALUES (10f88232-1ae7-4d88-a6a2-dfcebb22a596,Harper,Lee)
''', authors_data)

