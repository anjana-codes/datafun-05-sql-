
---- Query group-by 
-- Count the number of books by each author
select author_id, count(*) as book_count
from books
group by author_id;