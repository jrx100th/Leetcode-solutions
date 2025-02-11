-- Write your PostgreSQL query statement below
SELECT 
id,
SUM(CASE
    WHEN month = 'Jan' THEN revenue 
    ELSE null 
END) AS Jan_Revenue,
SUM(CASE
    WHEN month = 'Jan' THEN revenue 
    ELSE null 
END) AS Jan_Revenue,
SUM(CASE
    WHEN month = 'Jan' THEN revenue 
    ELSE null 
END) AS Jan_Revenue,
SUM(CASE
    WHEN month = 'Jan' THEN revenue 
    ELSE null 
END) AS Jan_Revenue,
FROM Department
GROUP BY id