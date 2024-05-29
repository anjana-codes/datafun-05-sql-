
--query_inner_join_authors_books 
select a.first, a.last, b.title, b.year_published
from authors a
inner join books b on a.author_id = b.author_id;