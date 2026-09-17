SELECT 
    w.id
FROM 
    Weather w JOIN Weather t
ON DATEDIFF(w.recordDate, t.recordDate) = 1
WHERE 
    w.temperature > t.temperature;