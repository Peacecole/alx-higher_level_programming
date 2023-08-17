-- Create a given table in a MySQL server with given field descript    ions
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
