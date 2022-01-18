
SELECT  CustomerId, 
        FirstName || ' ' || LastName AS FullName, 
        UPPER(City) || ' ' || UPPER(Country) AS Location
FROM    customers
WHERE   CustomerId = 16;


SELECT  EmployeeId, 
        FirstName, 
        LastName,
        LOWER(SUBSTR(FirstName, 1,4) || SUBSTR(LastName, 1,2)) AS NewId
FROM    employees;


SELECT  FirstName, 
        LastName, 
        (STRFTIME('%Y', 'now') - STRFTIME('%Y', HireDate)) - (STRFTIME('%m-%d', 'now') < STRFTIME('%m-%d', HireDate))
            AS Years
FROM    employees
WHERE   Years >=15
ORDER BY LastName ASC;


SELECT  COUNT(*) as NoFax
FROM    customers
WHERE   Fax IS NULL;

SELECT  CustomerId, 
        City, 
        COUNT(*) as total_num
FROM    customers
GROUP BY City
ORDER BY total_num DESC;


SELECT  invoices.InvoiceId ,
        customers.FirstName, 
        customers.LastName, 
        customers.FirstName || customers.LastName || invoices.InvoiceId AS InvoiceId
FROM    customers
INNER JOIN  invoices
ON          customers.CustomerId = invoices.CustomerId
WHERE       customers.FirstName = 'Astrid';