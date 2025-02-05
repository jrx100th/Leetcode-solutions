-- Write your PostgreSQL query statement below
SELECT query_name, 
ROUND((SUM(rating*1.0/position*1.0))/COUNT(query_name)*1.0,2) AS quality,
COALESCE(ROUND((
    SELECT COUNT(rating) FROM Queries q1
    WHERE rating < 3 AND q1.query_name = q2.query_name
    GROUP BY query_name
    )*100.0/(
        SELECT COUNT(rating) FROM Queries q3
        WHERE q3.query_name = q2.query_name
        GROUP BY query_name
    )*1.0,2),0) AS poor_query_percentage
FROM Queries q2
GROUP BY query_name