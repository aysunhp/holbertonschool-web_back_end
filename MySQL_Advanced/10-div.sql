-- Create a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END $$

<<<<<<< HEAD
DELIMITER ;
=======
DELIMITER ;
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
