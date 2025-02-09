-- Write your PostgreSQL query statement below
SELECT department, employee, salary FROM
(SELECT 
Department.name AS Department,
Employee.name AS Employee, salary AS Salary,
DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rank
FROM 
Employee
LEFT JOIN Department
ON Employee.departmentId = Department.id)
WHERE rank < 4