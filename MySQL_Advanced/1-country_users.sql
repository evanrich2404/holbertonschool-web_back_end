-- Creates the 'users' table.
-- This script is written with a generic SQL syntax in mind, but may require slight modifications based on the target database.

-- Check if the 'users' table already exists before trying to create it.
-- This is to avoid errors when the script runs on a database where the table already exists.
CREATE TABLE IF NOT EXISTS users (

    -- 'id' attribute:
    -- An integer that is never null, auto-increments, and serves as the primary key for the table.
    id INT NOT NULL AUTO_INCREMENT,

    -- 'email' attribute:
    -- A string with a maximum length of 255 characters, which is never null.
    -- The UNIQUE constraint ensures that every email in the table is distinct.
    email VARCHAR(255) NOT NULL UNIQUE,

    -- 'name' attribute:
    -- A string with a maximum length of 255 characters.
    name VARCHAR(255),

    -- 'country' attribute:
    -- An enumeration with values 'US', 'CO', and 'TN'.
    -- If not provided, the default value will be 'US' (the first element of the enumeration).
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',

    -- Primary key constraint for the 'id' attribute.
    PRIMARY KEY (id)
);

-- Notes:
-- 1. The 'IF NOT EXISTS' clause ensures the table will only be created if it doesn't exist.
--    Supported in databases like SQLite, PostgreSQL, and MySQL.
-- 2. The 'AUTO_INCREMENT' keyword is for MySQL. For PostgreSQL, consider using 'SERIAL'.
--    For SQLite, consider using 'INTEGER PRIMARY KEY AUTOINCREMENT'.
-- 3. The 'ENUM' data type is used to define columns that can only have one of the specified values.
--    Note: While ENUM is supported in MySQL, not all databases support it.
--    For databases that don't, you'll need to use VARCHAR or CHAR with a CHECK constraint.
