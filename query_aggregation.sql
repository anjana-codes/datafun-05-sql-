
---- Query to perform aggregation functions on the books table

select 
count(*) as total_books,
avg(year_published) as average_year_published,
min(year_published) as earliset_year,
max(year_published) as latest_year 
from books;