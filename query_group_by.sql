
-- Total number of books published each year
select year_published, count(*) as total_books
from books
group by year_published
order by year_published;