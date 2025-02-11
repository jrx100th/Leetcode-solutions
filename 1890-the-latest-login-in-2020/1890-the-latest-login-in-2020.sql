-- Write your PostgreSQL query statement below
SELECT Logins.user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE 
TO_CHAR(time_stamp, 'YYYY') = '2020'
GROUP BY Logins.user_id