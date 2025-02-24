-- Write your PostgreSQL query statement below

(SELECT name AS results
FROM Users u1
INNER JOIN 
MovieRating m1
ON u1.user_id = m1.user_id
GROUP BY name
ORDER BY COUNT(name) DESC, name ASC
LIMIT 1)
UNION ALL
(SELECT title 
FROM Movies m2
INNER JOIN
MovieRating m3
ON m2.movie_id = m3.movie_id
WHERE TO_CHAR(created_at,'yyyy-mm') = '2020-02'
GROUP BY title
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1
)