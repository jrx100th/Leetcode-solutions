-- Write your PostgreSQL query statement below
/*
SELECT 
(
    SELECT user_id FROM Users
    WHERE Users.user_id = Orders.buyer_id
) AS buyer_id,
(
    SELECT join_date FROM Users
    WHERE Users.user_id = Orders.buyer_id
) AS join_date,
COUNT(order_id) AS orders_in_2019
FROM
Orders
WHERE TO_CHAR(order_date,'yyyy') = '2019'
GROUP BY buyer_id
*/

SELECT
buyer_id,
join_date,
SUM(
    CASE WHEN TO_CHAR(order_date,'yyyy') = '2019' THEN 1
    ELSE 0
    END
) AS orders_in_2019
FROM Users
LEFT JOIN
Orders ON 
Users.user_id = Orders.buyer_id
GROUP BY buyer_id, join_date
