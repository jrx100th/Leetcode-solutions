-- Write your PostgreSQL query statement below
SELECT * FROM
(SELECT employee_id FROM Employees 
WHERE employee_id NOT IN
(SELECT t1emp FROM
(SELECT e1.employee_id AS t1emp , name AS t1name , s1.employee_id AS t2emp, salary AS t2sal FROM Employees e1
JOIN Salaries s1
ON e1.employee_id = s1.employee_id
AND s1.employee_id = e1.employee_id
))
UNION 
SELECT employee_id FROM Salaries 
WHERE employee_id NOT IN
(SELECT t1emp FROM
(SELECT e1.employee_id AS t1emp , name AS t1name , s1.employee_id AS t2emp, salary AS t2sal FROM Employees e1
JOIN Salaries s1
ON e1.employee_id = s1.employee_id
AND s1.employee_id = e1.employee_id
)))
ORDER BY 1 ASC