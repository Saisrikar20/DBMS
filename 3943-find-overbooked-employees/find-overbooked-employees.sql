# Write your MySQL query statement below
SELECT
e.employee_id,
e.employee_name,
e.department,
COUNT(*) AS meeting_heavy_weeks
FROM employees e
JOIN (
    SELECT
    employee_id,
    DATE_SUB(meeting_date, INTERVAL WEEKDAY(meeting_date) DAY) AS week_start,
    SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY employee_id, week_start
    HAVING SUM(duration_hours) > 20
) w ON e.employee_id = w.employee_id
GROUP BY e.employee_id, e.employee_name, e.department
HAVING COUNT(*) >= 2
ORDER BY meeting_heavy_weeks DESC, e.employee_name ASC;
