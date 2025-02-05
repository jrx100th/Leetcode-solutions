-- Write your PostgreSQL query statement below

SELECT
  contest_id,
  ROUND(
    COUNT(user_id) * 100.0 / (
      SELECT COUNT(*)
      FROM Users
    ),
    2
  ) AS percentage
FROM Register
GROUP BY 1
ORDER BY percentage DESC, contest_id;



/*
SELECT 
DISTINCT(contest_id),
(ROUND((
    SELECT COUNT(user_id) FROM Register r2
    WHERE r1.contest_id = r2.contest_id
    GROUP BY contest_id
)*100.0/(
    SELECT COUNT(DISTINCT(user_id)) FROM Users
),2)) AS percentage
FROM Register r1
LEFT JOIN Users u1
ON r1.user_id = u1.user_id
ORDER BY percentage DESC, contest_id
*/