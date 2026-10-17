WITH RankedReviews AS (
    SELECT
        employee_id,
        rating,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id
            ORDER BY review_date DESC, review_id DESC
        ) AS rn
    FROM performance_reviews
),
LastThree AS (
    SELECT
        employee_id,
        MAX(CASE WHEN rn = 1 THEN rating END) AS latest_rating,
        MAX(CASE WHEN rn = 2 THEN rating END) AS second_rating,
        MAX(CASE WHEN rn = 3 THEN rating END) AS earliest_rating,
        COUNT(*) AS review_count
    FROM RankedReviews
    WHERE rn <= 3
    GROUP BY employee_id
)
SELECT
    e.employee_id,
    e.name,
    l.latest_rating - l.earliest_rating AS improvement_score
FROM LastThree l
JOIN employees e
    ON e.employee_id = l.employee_id
WHERE l.review_count = 3
  AND l.earliest_rating < l.second_rating
  AND l.second_rating < l.latest_rating
ORDER BY improvement_score DESC, e.name ASC;