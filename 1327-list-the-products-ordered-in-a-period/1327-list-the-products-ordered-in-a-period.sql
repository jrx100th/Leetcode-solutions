-- Write your PostgreSQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM Products
INNER JOIN Orders
ON Products.product_id = Orders.product_id
WHERE TO_CHAR(order_date, 'yyyy-mm') = '2020-02'
GROUP BY product_name
HAVING SUM(unit) >= 100