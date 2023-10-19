-- AddBonus : adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(IN student_id INT, IN project_name VARCHAR(255), IN bonus INT)
BEGIN
    DECLARE project_id INT;

    -- Get the project id.
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Add the bonus.
    INSERT INTO corrections (student_id, project_id, bonus) VALUES (student_id, project_id, bonus);
END //
DELIMITER ;
