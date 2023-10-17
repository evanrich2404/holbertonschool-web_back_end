-- Creates the 'users' table.
-- This script is written with a generic SQL syntax in mind, but may require slight modifications based on the target database.

-- Check if the 'users' table already exists before trying to create it.
-- This is to avoid errors when the script runs on a database where the table already exists.
CREATE TABLE IF NOT EXISTS users (

    -- 'id' attribute:
    -- An integer that is never null, auto-increments (acts as a counter that increases by 1 each time a new record is added),
    -- and serves as the primary key for the table.
    id INT NOT NULL AUTO_INCREMENT,

    -- 'email' attribute:
    -- A string with a maximum length of 255 characters, which is never null.
    -- The UNIQUE constraint ensures that every email in the table is distinct, enforcing business rules.
    email VARCHAR(255) NOT NULL UNIQUE,

    -- 'name' attribute:
    -- A string with a maximum length of 255 characters.
    name VARCHAR(255),

    -- Primary key constraint for the 'id' attribute.
    PRIMARY KEY (id)
);

-- Notes:
-- 1. The 'IF NOT EXISTS' clause ensures the table will only be created if it doesn't exist.
--    Supported in databases like SQLite, PostgreSQL, and MySQL.
-- 2. The 'AUTO_INCREMENT' keyword is for MySQL. For PostgreSQL, consider using 'SERIAL'.
--    For SQLite, consider using 'INTEGER PRIMARY KEY AUTOINCREMENT'.
-- 3. 'VARCHAR(255)' is a common syntax for a variable-length string up to 255 characters.
