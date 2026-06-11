<<<<<<< HEAD
-- Make a table with enum
=======
-- Create users table with country enum
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
<<<<<<< HEAD
    country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
)
=======
    country ENUM('US','CO','TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY(id)
);
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
