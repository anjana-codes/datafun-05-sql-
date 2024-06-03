
--query_inner_join_authors_books 
SELECT a.first, a.last, b.title, b.year_published
FROM authors a
INNER JOIN books b on a.author_id = b.author_id;