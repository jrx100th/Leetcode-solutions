WITH min_dates AS (
    SELECT 
        customer_id, 
        MIN(order_date) AS min_order_date, 
        MIN(customer_pref_delivery_date) AS min_pref_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT 
    ROUND(((SUM(CASE 
            WHEN min_order_date = min_pref_date THEN 1.0
            ELSE 0
        END)*1.0/
        COUNT(DISTINCT(customer_id))*1.0)*100),2) AS immediate_percentage
FROM min_dates
;
