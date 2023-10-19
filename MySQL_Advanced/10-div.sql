-- SafeDiv : divides and returns the first by the second number (or returns 0 if 2nd is 0)
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //
DELIMITER ;
