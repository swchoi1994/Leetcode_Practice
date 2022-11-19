# Write your MySQL query statement below
SELECT 
    customers.name as 'Customers'
FROM
    Customers
WHERE
    customers.id not in
(
    SELECT customerid from orders    
);