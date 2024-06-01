
-- Total number of books published each year
SELECT year_published, COUNT(*) as total_books
FROM books
GROUP BY year_published
ORDER BY year_published;