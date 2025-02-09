SELECT 
CASE WHEN COUNT(*) > 1 THEN 
    (SELECT salary  FROM
    (
    SELECT 
    salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS rank
    FROM Employee
    )
    WHERE rank = 2)
    ELSE null
END AS "SecondHighestSalary"
FROM Employee