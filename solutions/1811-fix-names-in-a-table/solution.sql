SELECT user_id,
    CONCAT(UPPER(LEFT(name,1)),LOWER(RIGHT(name,length(name)-1))) name
FROM Users
ORDER BY user_id
