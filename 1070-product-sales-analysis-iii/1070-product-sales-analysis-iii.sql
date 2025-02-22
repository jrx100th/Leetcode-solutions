SELECT 
DISTINCT(product_id) AS product_id,
year AS first_year,
quantity,
price
FROM Sales s1
WHERE year IN (
    SELECT MIN(year) FROM Sales s2
    WHERE s1.product_id = s2.product_id
)
