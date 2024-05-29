-- Update records in the authors table when first name contains 'a'
update authors
set first = 'Anjana', last = 'Dhakal'
where first = 'F. Scott';

update books
set title = 'The Great Mountains'
where year_published = '1960';
