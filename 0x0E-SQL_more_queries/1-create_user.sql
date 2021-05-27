-- Create user with all privileges
DROP USER 'user_0d_1'@'localhost';

CREATE USER 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
