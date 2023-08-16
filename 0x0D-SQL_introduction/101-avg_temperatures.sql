-- Imports into a database a given table
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `tempaeratures`
GROUP BY `city`
RDER BY `avg_temp` DESC;
