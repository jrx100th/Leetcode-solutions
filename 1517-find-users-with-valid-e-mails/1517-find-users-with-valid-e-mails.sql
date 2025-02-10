-- Write your PostgreSQL query statement below
SELECT 
user_id,
name,
mail
FROM Users
WHERE 
RIGHT(mail,13) = '@leetcode.com'
AND
mail NOT LIKE '%#%'
AND
LEFT(mail,1) NOT IN ('.','#','_','-')