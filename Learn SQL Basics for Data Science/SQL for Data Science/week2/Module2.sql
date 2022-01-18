SELECT *
FROM tracks
WHERE Milliseconds >= 5000000;

SELECT *
FROM invoices
WHERE total BETWEEN 5 and 15;

SELECT *
FROM customers
WHERE State IN ('RJ','DF', 'AB', 'BC', 'CA', 'WA','NY') 
AND FirstName = 'Jack';

SELECT *
FROM invoices
WHERE CustomerId IN (56,58)
AND Total BETWEEN 1 AND 5
AND InvoiceId = '315';

SELECT *
FROM tracks
WHERE name LIKE 'All%';

SELECT *
FROM customers
WHERE email LIKE 'J%@gmail.com';

SELECT *
FROM invoices
WHERE BillingCity IN ('Brasilia', 'Edmonton', 'Vancouver')
ORDER BY invoiceId DESC;

SELECT  customerId, 
        COUNT(*)
FROM    invoices
GROUP BY customerId
ORDER BY COUNT(*) DESC;

SELECT  AlbumID,
        COUNT(*) as New
FROM    tracks
GROUP BY AlbumId
HAVING New >=12

