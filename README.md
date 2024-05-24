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

### Git add and commit
```
git add .
git commit -m "initial work"
git push origin main
```

## Source
This project was built to the following specifications: https://github.com/denisecase/datafun-05-spec
