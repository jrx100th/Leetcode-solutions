-- Write your PostgreSQL query statement below
SELECT 
user_id,
email
--SUBSTRING(email FROM )
FROM Users
WHERE RIGHT(email,4) = '.com'
AND email LIKE '%@%'
AND LEFT(email,POSITION('@' IN email)-1) ~ '^[a-zA-Z0-9_]+$'
--AND RIGHT(LEFT(email, POSITION('.' IN email)-1),POSITION('@' IN email)) ~ '^[a-zA-Z]+$'