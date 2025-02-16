-- Write your PostgreSQL query statement below
SELECT user_id as buyer_id, MAX(join_date) as join_date,
COUNT(CASE WHEN o.order_date BETWEEN '2019-01-01' AND '2019-12-31' THEN 1 ELSE NULL END) AS orders_in_2019 
FROM Users u LEFT JOIN Orders o ON u.user_id = o.buyer_id
GROUP BY user_id
