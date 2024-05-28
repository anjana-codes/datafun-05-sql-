# Project 5: datafun-05-sql-

Title : Specification for Project 5 SQL Module

Anjana Dhakal, May 22, 2024

## Overview
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Objectives 
Create a Python script that demonstrates the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback.

## Create GitHub Repository and clone to VS Code
 #create GitHub repository
```
 GitHub Repository: datafun-05-sql-
 Documentation: README.md
```
#clone to VS Code
```
git clone site_URL
```
## Adding files 
- Add a .py file to work in.
- Add a requirements.txt file to hold the required project modules.
- Create a .venv to act as the virtual environment.
- Include a .gitignore file to exclude the .venv file from the rest of the Python environment.

## Create Project Virtual Environment
```
 py -m venv .venv
source .\.venv\Scripts\activate
```

## Install all Required Packages
```
 py -m pip install pandas pyarrow
 py -m pip freeze > requirements.txt
```

## Import Dependencies 
```
import sqlite3
import pandas as pd
import pathlib
```
## Add data folder and .csv
Added a data folder to the project folder, then added two .csv files (authors and books) in VS Code.

## Create Database(db)
```
 # Define the database file in the current root project directory
 db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()
```
## created create_tables.sql
```
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT,
    last TEXT
);
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
```
## created book_manager.py
```
import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """ Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-\\create_tables.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """ Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
```
 
## Git add and commit
```
git add .
git commit -m "Database interaction using SQLite Explorer"
git push origin main
```

## Source
This project was built to the following specifications: https://github.com/denisecase/datafun-05-spec
