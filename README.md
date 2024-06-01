# Project 5: datafun-05-sql-

Title : Specification for Project 5 SQL Module

Anjana Dhakal, May 22, 2024(updated May 29, 2024)

## Overview
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Objectives 
Create a Python script that demonstrates the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback.

## Create GitHub Repository and clone to VS Code
 #create GitHub repository
```
 GitHub Repository: datafun-05-sql-
 Documentation: README.me
 Initialize script: db_initialize_anjana.py
 Operations script: db_operations_anjana.py

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
## Git add and commit
```
git add .
git commit -m "Database interaction using SQLite Explorer"
git push origin main
```
## Add Folder and files 
```
Add a data folder to the project folder, then added two .csv files (authors and books) in VS Code.
Add book_manager.py file to create a database, and fill with inofrmation from CSV files. 
```
## Worked on Different SQL Operations
Implement SQL statements and queries to perform additional operations and use Python to execute SQL statements.

1. Create create_tables.sql
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
2. Create insert_data.sql file
```
INSERT INTO authors (author_id, first_name, last_name) VALUES

INSERT INTO books (book_id, title, year_published, author_id) VALUES

```
3. Create select_records.sql file
```
#select all records from the authors table
SELECT * FROM authors;

#select all records from the books table
SELECT * FROM books;
```
4. Create update_records.sql file
```
#update records in the authors table where first name contains 'F. Scott'

UPDATE authors
SET first = 'Anjana', last = 'Dhakal'
WHERE first = 'F. Scott';

#update records in the books table where year_published is 1960

UPDATE books
SET title = 'The Great Mountains'
WHERE year_published = '1960';
```
5. Create delete_records.sql file
```
#delete records from the authors table where first name is Anjana and last name Dhakal
DELETE FROM authors
WHERE first = 'Anjana' AND last = 'Dhakal';

#delete records from the books table where title is "The Great Mountains"
DELETE FROM  books
WHERE title = 'The Great Mountains' ;
```
6. Create query_aggregation.sql file
```
SELECT 
COUNT(*) as total_books,
AVG(year_published) as average_year_published
FROM books;
```
7. Create query_filter.sql files
```
SELECT first, last FROM authors 
WHERE first LIKE 'j%';
```
8. Create query_sorting.sql file
```
SELECT * FROM books
ORDER BY year_published DESC;

```
9. Create query_group_by.sql file
```
SELECT year_published, COUNT(*) as total_books
FROM books
GROUP BY year_published
ORDER BY year_published;
```
10. Create query_join.sql file
```
SELECT a.first, a.last, b.title, b.year_published
FROM authors a
INNER JOIN books b on a.author_id = b.author_id;
```

## Repeat Git add and commit
```
git add .
git commit -m "project is done"
git push origin main
```

## Source
This project was built to the following specifications: https://github.com/denisecase/datafun-05-spec
