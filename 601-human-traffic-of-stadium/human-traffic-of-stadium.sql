WITH Qualified AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM Qualified
WHERE grp IN (
    SELECT grp
    FROM Qualified
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;