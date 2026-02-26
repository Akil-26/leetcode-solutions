SELECT DISTINCT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id
