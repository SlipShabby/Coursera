SELECT  Name, 
        AlbumID
FROM    tracks
WHERE   AlbumID IN 
(
    SELECT  AlbumID
    FROM    albums
    WHERE   Title = 'Californication'
);

SELECT  FirstName, 
        LastName, 
        City, 
        Email, 
        COUNT(invoices.CustomerID) as invoice_num
FROM    customers
INNER JOIN  invoices
ON          customers.CustomerID = invoices.InvoiceID
GROUP BY    customers.CustomerID;

SELECT  tracks.Name, 
        albums.Title, 
        tracks.TrackId, 
        albums.ArtistId
FROM    tracks 

INNER JOIN  albums 
ON          tracks.AlbumId = albums.AlbumId
WHERE       tracks.TrackId = 12;


SELECT  manager.LastName as manager, 
        employees.LastName as employee
FROM    employees as manager 
INNER JOIN employees as employees
ON          employees.ReportsTo = manager.;


SELECT  artists.Name, 
        albums.Title, 
        albums.AlbumId
FROM    artists
LEFT JOIN   albums
ON          artists.ArtistId = albums.ArtistId
WHERE       albums.AlbumId IS NULL;


SELECT  FirstName, 
        LastName
FROM    employees
UNION
SELECT  FirstName, 
        LastName
FROM    customers
ORDER BY LastName DESC
LIMIT 6;

SELECT  c.FirstName, 
        c.LastName, 
        c.City, 
        i.BillingCity
FROM    customers c 
INNER JOIN  invoices i 
ON          c.CustomerID = i.CustomerID
WHERE       c.City != i.BillingCity;