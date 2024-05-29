-- Update records in the authors table when first name contains 'a'
UPDATE authors
SET first = 'Anjana', last = 'Dhakal'
WHERE first = 'F. Scott';

UPDATE books
SET title = 'The Great Mountains'
WHERE year_published = '1960';
