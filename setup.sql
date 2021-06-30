-- Create the database and user for the application.
CREATE DATABASE IF NOT EXISTS hbtn_col_db;
CREATE USER IF NOT EXISTS 'hbtn_col'@'localhost' IDENTIFIED BY 'hbtn_col_pwd';
GRANT ALL PRIVILEGES ON `hbtn_col_db`.* TO 'hbtn_col'@'localhost';
FLUSH PRIVILEGES;
