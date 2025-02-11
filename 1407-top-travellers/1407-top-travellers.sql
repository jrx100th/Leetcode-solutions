-- Write your PostgreSQL query statement below
SELECT Users.name,
COALESCE(SUM(Rides.distance),0) AS travelled_distance
FROM Users FULL JOIN Rides
ON Users.id = Rides.user_id
GROUP BY Users.name
ORDER BY travelled_distance DESC, Users.name