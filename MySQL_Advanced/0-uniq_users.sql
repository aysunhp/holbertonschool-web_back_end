<<<<<<< HEAD
-- Make a table, if table exist, you should not fail
CREATE TABLE IF NOT EXISTS users(
=======
-- Create users table with unique email
CREATE TABLE IF NOT EXISTS users (
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
<<<<<<< HEAD
)
=======
);
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
