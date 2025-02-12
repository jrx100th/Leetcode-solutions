SELECT person_name FROM
(SELECT person_name, summ FROM
(   
    SELECT 
    person_name,
    SUM(weight) OVER(ORDER BY turn) AS summ
    FROM Queue
)
WHERE summ <= 1000
ORDER BY summ DESC
LIMIT 1
)