SELECT 
ROUND(
    COUNT(DISTINCT a.player_id)/
    (SELECT COUNT(DISTINCT player_id) FROM Activity)
    ,2
) AS fraction
FROM 
(   SELECT player_id,MIN(event_date) AS first_login 
    FROM Activity
    GROUP BY player_id
) a
JOIN Activity b
ON a.player_id = b.player_id 
AND b.event_date = DATE_ADD(a.first_login,INTERVAL 1 DAY) 
