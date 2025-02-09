SELECT 
    CASE
        WHEN (
            SELECT COUNT(*) 
            FROM MyNumbers
            GROUP BY num
            HAVING COUNT(num) = 1
            ORDER BY num DESC
            LIMIT 1
        ) = 1 THEN (
            SELECT MAX(num)
            FROM MyNumbers
            GROUP BY num
            HAVING COUNT(num) = 1
            ORDER BY num DESC
            LIMIT 1
        )
        ELSE NULL
    END AS num
FROM MyNumbers
LIMIT 1;
