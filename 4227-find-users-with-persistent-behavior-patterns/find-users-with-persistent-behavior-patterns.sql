WITH daily AS (
SELECT user_id, action_date, MIN(action) AS action
FROM activity
GROUP BY user_id, action_date
HAVING COUNT(*) = 1
),
grp AS (
SELECT
user_id,
action,
action_date,
DATE_SUB(action_date, INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id, action ORDER BY action_date) DAY) AS grp_key
FROM daily
),
streaks AS (
SELECT
user_id,
action,
COUNT(*) AS streak_length,
MIN(action_date) AS start_date,
MAX(action_date) AS end_date
FROM grp
GROUP BY user_id, action, grp_key
HAVING COUNT(*) >= 5
),
ranked AS (
SELECT *,
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY streak_length DESC, start_date ASC) AS rn
FROM streaks
)
SELECT user_id, action, streak_length, start_date, end_date
FROM ranked
WHERE rn = 1
ORDER BY streak_length DESC, user_id ASC;