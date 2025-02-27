SELECT e2.employee_id,
e2.name, COUNT(e2.employee_id) AS reports_count, 
ROUND(AVG(e1.age),0) AS average_age
FROM Employees e1
INNER JOIN Employees e2
ON e1.reports_to = e2.employee_id
GROUP BY e2.employee_id,e2.name
ORDER BY employee_id;