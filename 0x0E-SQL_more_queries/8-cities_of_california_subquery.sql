-- Lists records with given field values
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
