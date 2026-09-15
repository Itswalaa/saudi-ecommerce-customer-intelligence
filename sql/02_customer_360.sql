-- Create Customer 360 Aggregations Layer
DROP TABLE IF EXISTS customer_360;

CREATE TABLE customer_360 AS
WITH customer_aggregates AS (
    SELECT 
        c.customer_id,
        c.city,
        c.age,
        c.acquisition_channel,
        DATE(c.signup_date) AS signup_date,
        MIN(o.order_date) AS first_order_date,
        MAX(o.order_date) AS last_order_date,
        COUNT(o.order_id) AS total_orders,
        COALESCE(SUM(o.order_amount), 0) AS total_revenue,
        COALESCE(AVG(o.order_amount), 0) AS aov,
        CAST((JULIANDAY('2025-12-31') - JULIANDAY(MAX(o.order_date))) AS INTEGER) AS recency
    FROM customers c
    LEFT JOIN clean_orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
)
SELECT 
    *,
    total_orders AS frequency,
    total_revenue AS monetary
FROM customer_aggregates;
