import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-\\project.db"

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
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
            sql_file = "C:\\Users\\AnjanaD\\Documents\\datafun-05-sql-\\insert_records.sql"
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
            sql_file = pathlib.Path("update_records.sql")
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
            sql_file = pathlib.Path("select_records.sql")
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
            sql_file = pathlib.Path("delete_records.sql")
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
            sql_file = pathlib.Path("query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            result = cursor.fetchone()
            print("total_books:", result[0])
            print("average_year_published:", round(result[1]))
            print("earliest_year:", round(result[2]), "characters.")
            print("latest_year:", round(result[2]), "characters.")
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

def query_filter():
    """Function to filter authors data based on conditions"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_filter.sql")
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
            sql_file = pathlib.Path("query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[1], book[2])  # Print year_published 
    except sqlite3.Error as e:
        print("Error sorting book data:", e)


def main():
    insert_data_from_csv()
    insert_records()
    update_records()
    select_records()
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
  

if __name__ == "__main__":
    main()