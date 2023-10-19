-- Creates the 'users' table.
-- Check if the 'users' table already exists before trying to create it.
-- This is to avoid errors when the script runs on a database where the table already exists.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
