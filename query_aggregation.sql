
---- Query to perform aggregation functions on the books table

SELECT
COUNT(*) as total_books,
AVG(year_published) as average_year_published
FROM books;