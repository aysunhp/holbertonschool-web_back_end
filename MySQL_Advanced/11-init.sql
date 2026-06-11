DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
<<<<<<< HEAD
INSERT INTO students (name, score) VALUES ("Alexa", 130);
=======
INSERT INTO students (name, score) VALUES ("Alexa", 130);
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
