'''
Title: Specification for Project 5 SQL Module

Overview:
Here, I created a databse, added tables to the databse, filled the tables with data from both CSV and .sql files.
Then worked on different SQL operations like update, delete, sorting, join etc. 
All of this is doccumented in the README.
'''
import sqlite3
import pandas as pd
import pathlib
import logging 


# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method

# Define the database file in the current root project directory
db_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-\\project.db"

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data").joinpath("authors.csv")
        book_data_path = pathlib.Path("data").joinpath("books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # Use the pandas DataFrame to_sql() method to insert data
            # Pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data from CSV:", e)

def insert_records():
    """Function to read and execute SQL statements to insert data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("insert_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)

def update_records():
    """Function to update one or more records in the authors table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records updated successfully.")
    except sqlite3.Error as e:
        print("Error updating records:", e)

        
def select_records():
    """Function to update one or more records in the authors table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("select_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records read successfully.")
    except sqlite3.Error as e:
        print("Error reading records:", e)


def delete_records():
    """Function to delete one or more records in the authors table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting records:", e)

def query_aggregation():
    """Function to perform aggregation functions on the books table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            result = cursor.fetchone()
            print("total_books:", result[0])
            print("average_year_published:", round(result[1]))
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

def query_filter():
    """Function to filter authors data based on conditions"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("query_filter.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            results = cursor.fetchall()
            for row in results:
                print(row)  
    except sqlite3.Error as e:
        print("Error filtering book data:", e)

def query_sorting():
    """Function to sort book data based on publication date"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[1], book[2])  # Print title and year_published 
    except sqlite3.Error as e:
        print("Error sorting book data:", e)

def query_group_by():
    """Function to execute SQL query with GROUP BY clause and display the count of each grouping."""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("query_group_by.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.cursor()
            cursor.execute(sql_script)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))
            print("-" * (len(" | ".join(column_names)) + 10))
            for row in results:
             print(" | ".join(map(str, row))) 
    except sqlite3.Error as e:
        print("Error executing query:", e)

def query_join():
    """Function to read and execute SQL statements to perform INNER JOIN and display the results"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql").joinpath("query_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))
            print("-" * (len(" | ".join(column_names)) + 10))
            for row in results:
             print(" | ".join(map(str, row)))
    except sqlite3.Error as e:
        print("Error executing query:", e)      

def main():
    insert_data_from_csv()
    insert_records()
    update_records()
    select_records()
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()

logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    logging.info("Program started") # add this at the beginning of the main method
    main()
    logging.info("Program ended")  # add this at the end of the main method