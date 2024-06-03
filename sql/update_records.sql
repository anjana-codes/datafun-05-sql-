-- Update records in the authors table 
UPDATE authors
SET first = 'Anjana', last = 'Dhakal'
WHERE first = 'F. Scott';

--Update records in the books table
UPDATE books
SET title = 'The Great Mountains'
WHERE year_published = '1960';
