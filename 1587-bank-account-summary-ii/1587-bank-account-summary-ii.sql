-- Write your PostgreSQL query statement below
SELECT 
name AS "NAME",
SUM(amount) AS "BALANCE"
FROM
Users
LEFT JOIN
Transactions
ON 
Users.account = Transactions.account
GROUP BY name
HAVING SUM(amount) > 10000