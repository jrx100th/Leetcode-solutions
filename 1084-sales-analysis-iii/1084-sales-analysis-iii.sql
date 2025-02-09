SELECT
    product_id,(
        SELECT product_name FROM Product
        WHERE Sales.product_id = product_id
    )
FROM Sales
WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY product_id
HAVING NOT EXISTS (
    SELECT 1
    FROM Sales s2
    WHERE s2.product_id = Sales.product_id
    AND (s2.sale_date < '2019-01-01' OR s2.sale_date > '2019-03-31')
);
