SELECT name,SUM(amount)AS balance 
FROM Users U 
JOIN Transactions T ON U.account=T.account 
GROUP BY T.account 
HAVING sum(amount)>10000;