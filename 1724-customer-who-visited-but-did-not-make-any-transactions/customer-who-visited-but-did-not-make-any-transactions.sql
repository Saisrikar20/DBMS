SELECT
    V.customer_id,
    COUNT(V.visit_id) AS count_no_trans
FROM Transactions T
RIGHT JOIN Visits V
ON T.visit_id=V.visit_id
WHERE T.transaction_id IS NULL
GROUP BY customer_id;

