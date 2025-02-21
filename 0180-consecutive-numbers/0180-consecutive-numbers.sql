
SELECT
DISTINCT(num) AS "ConsecutiveNums"
FROM 
Logs l1
WHERE num = (
    SELECT num FROM Logs l2
    WHERE l1.id = l2.id+1
)
AND num = (
    SELECT num FROM Logs l3
    WHERE l1.id = l3.id-1
)
