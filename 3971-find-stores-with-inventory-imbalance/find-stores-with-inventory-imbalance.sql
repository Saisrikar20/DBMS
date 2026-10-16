 WITH ranked AS (
    SELECT i.store_id, i.product_name, i.quantity, i.price,
    ROW_NUMBER() OVER (PARTITION BY i.store_id ORDER BY i.price DESC) AS expensive_rank,
    ROW_NUMBER() OVER (PARTITION BY i.store_id ORDER BY i.price ASC) AS cheap_rank,
    COUNT(*) OVER (PARTITION BY i.store_id) AS product_count
    FROM inventory i
 ),
 imbalance AS (
    SELECT store_id,
    MAX(CASE WHEN expensive_rank = 1 THEN product_name END) AS most_exp_product,
    MAX(CASE WHEN cheap_rank = 1 THEN product_name END) AS cheapest_product,
    MAX(CASE WHEN expensive_rank = 1 THEN quantity END) AS expensive_quantity,
    MAX(CASE WHEN cheap_rank = 1 THEN quantity END) AS cheapest_quantity,
    MAX(product_count) AS product_count
    FROM ranked
    GROUP BY store_id
 )
 SELECT s.store_id, s.store_name, s.location,
 i.most_exp_product, i.cheapest_product,
 ROUND(i.cheapest_quantity / i.expensive_quantity, 2) AS imbalance_ratio
 FROM imbalance i
 JOIN stores s ON s.store_id = i.store_id
 WHERE i.product_count >= 3
 AND i.expensive_quantity < i.cheapest_quantity
 ORDER BY imbalance_ratio DESC, s.store_name ASC;
