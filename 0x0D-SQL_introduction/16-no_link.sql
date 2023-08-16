-- Lists all the records of a table with given field values
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
