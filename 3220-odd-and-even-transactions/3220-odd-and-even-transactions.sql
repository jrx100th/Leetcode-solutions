SELECT 
    t11.transaction_date,
    -- Sum of odd amounts (where amount is odd)
    COALESCE(
        (SELECT SUM(amount) 
         FROM transactions t2
         WHERE t2.transaction_date = t11.transaction_date AND t2.amount % 2 = 1),
        0
    ) AS odd_sum,
    -- Sum of even amounts (where amount is even)
    SUM(CASE WHEN t11.amount % 2 = 0 THEN t11.amount ELSE 0 END) AS even_sum
FROM transactions t11
GROUP BY t11.transaction_date
ORDER BY transaction_date