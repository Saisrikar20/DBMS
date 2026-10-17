WITH UserStats AS (
    SELECT
        user_id,
        MAX(event_date) AS last_event_date,
        MIN(event_date) AS first_event_date,
        MAX(monthly_amount) AS max_historical_amount,
        MAX(CASE
            WHEN event_type = 'downgrade' THEN 1
            ELSE 0
        END) AS has_downgrade
    FROM subscription_events
    GROUP BY user_id
),
LatestEvent AS (
    SELECT
        user_id,
        event_type,
        plan_name,
        monthly_amount,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC, event_id DESC
        ) AS rn
    FROM subscription_events
)
SELECT
    s.user_id,
    l.plan_name AS current_plan,
    l.monthly_amount AS current_monthly_amount,
    s.max_historical_amount,
    DATEDIFF(s.last_event_date, s.first_event_date) AS days_as_subscriber
FROM UserStats s
JOIN LatestEvent l
    ON s.user_id = l.user_id
WHERE l.rn = 1
    AND l.event_type <> 'cancel'
    AND s.has_downgrade = 1
    AND l.monthly_amount < 0.5 * s.max_historical_amount
    AND DATEDIFF(s.last_event_date, s.first_event_date) >= 60
ORDER BY days_as_subscriber DESC, s.user_id ASC;
