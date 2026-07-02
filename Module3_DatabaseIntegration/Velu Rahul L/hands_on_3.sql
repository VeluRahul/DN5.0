-- TASK 35 - students enrolled in more courses than the average:

SELECT s.student_id,CONCAT(s.first_name,' ',s.last_name) AS Student_Name,COUNT(e.course_id) AS Total_Courses FROM students s INNER JOIN enrollments e ON s.student_id = e.student_id GROUP BY s.student_id,s.first_name,s.last_name HAVING COUNT(e.course_id) > ( SELECT AVG(course_count) FROM ( SELECT COUNT(course_id) AS course_count FROM enrollments GROUP BY student_id ) AS AvgEnrollment );

-- TASK 36 - Courses where every student scored 'A':

SELECT c.course_name,c.course_code FROM courses c WHERE NOT EXISTS ( SELECT * FROM enrollments e WHERE e.course_id = c.course_id AND e.grade <> 'A' );

-- TASK 37 - highest paid professor in each department:

SELECT p.prof_name,p.salary,d.dept_name FROM professors p INNER JOIN departments d ON p.department_id = d.department_id WHERE p.salary = ( SELECT MAX(p2.salary) FROM professors p2 WHERE p2.department_id = p.department_id );

-- TASK 38 - Departments having average professor salary > 85000:

SELECT * FROM ( SELECT d.department_id,d.dept_name,AVG(p.salary) AS Average_Salary FROM departments d INNER JOIN professors p ON d.department_id = p.department_id GROUP BY d.department_id,d.dept_name) AS DepartmentSalary WHERE Average_Salary > 85000;

-- TASK 39 - create student enrollment summary view:

CREATE VIEW vw_student_enrollment_summary AS SELECT s.student_id,CONCAT(s.first_name,' ',s.last_name) AS Student_Name,d.dept_name,COUNT(e.course_id) AS Total_Courses,ROUND(AVG(CASE WHEN e.grade='A' THEN 4 WHEN e.grade='B' THEN WHEN e.grade='C' THEN 2 WHEN e.grade='D' THEN 1 WHEN e.grade='F' THEN 0 ELSE NULL END),2) AS GPA FROM students s LEFT JOIN departments d ON s.department_id=d.department_id LEFT JOIN enrollments e ON s.student_id=e.student_id GROUP BY s.student_id,Student_Name,d.dept_name;

-- to view output

SELECT * FROM vw_student_enrollment_summary;

-- TASK 40 - create course statistic view:

CREATE VIEW vw_course_stats AS SELECT c.course_name,c.course_code,COUNT(e.student_id) AS Total_Enrollments,ROUND(AVG(CASE WHEN e.grade='A' THEN 4 WHEN e.grade='B' THEN 3 WHEN e.grade='C' THEN 2 WHEN e.grade='D' THEN 1 WHEN e.grade='F' THEN 0 END),2) AS Avg_GPA FROM courses c LEFT JOIN enrollments e ON c.course_id=e.course_id GROUP BY c.course_id,c.course_name,c.course_code;

-- to view output

SELECT * FROM vw_course_stats;

-- TASK 41 - students having GPA greater than 3

SELECT * FROM vw_student_enrollment_summary WHERE GPA > 3.0;

-- TASK 42 - Attempt UPDATE through View

/*
The following UPDATE may fail because the view is created using multiple tables with JOIN operations.Multi-table views are generally not updatable since the database cannot determine which underlying table should be modified.
*/

UPDATE vw_student_enrollment_summary SET GPA = 4 WHERE student_id = 1;

-- TASK 43 - drop Views:

DROP VIEW IF EXISTS vw_course_stats;

DROP VIEW IF EXISTS vw_student_enrollment_summary;

-- Recreate View using WITH CHECK OPTION:

CREATE VIEW vw_student_enrollment_summary AS SELECT student_id,first_name,last_name,department_id FROM students WHERE department_id = 1 WITH CHECK OPTION;

-- to view output

SELECT * FROM vw_student_enrollment_summary;

-- TASK 44 - stored procedure : enroll student

DELIMITER $$
CREATE PROCEDURE sp_enroll_student( IN p_student_id INT,IN p_course_id INT,IN p_enrollment_date DATE)

BEGIN

    IF EXISTS(

        SELECT * FROM enrollments WHERE student_id = p_student_id AND course_id = p_course_id

    )

    THEN

        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='Student is already enrolled in this course';

    ELSE

        INSERT INTO enrollments(student_id,course_id,enrollment_date,grade) VALUE (p_student_id,p_course_id,p_enrollment_date,NULL);

    END IF;

END $$

DELIMITER ;

-- Test procedure

CALL sp_enroll_student(2,2,'2024-07-01');

-- TASK 45 - Department Transfer Log Table:

CREATE TABLE department_transfer_log (log_id INT AUTO_INCREMENT PRIMARY KEY,student_id INT,old_department INT,new_department INT,transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Stored Procedure : Transfer Student:


DELIMITER $$

CREATE PROCEDURE sp_transfer_student(IN p_student_id INT, IN p_new_department INT)

BEGIN

    DECLARE oldDept INT;

    START TRANSACTION;

    SELECT department_id INTO oldDept FROM students WHERE student_id=p_student_id;

    UPDATE students SET department_id=p_new_department WHERE student_id=p_student_id;

    INSERT INTO department_transfer_log(student_id,old_department,new_department) VALUES (p_student_id,oldDept,p_new_department);

    COMMIT;

END $$

DELIMITER ;

-- Test Procedure:

CALL sp_transfer_student(3,1);

-- TASK 46 - Transaction with Rollback:

START TRANSACTION;

UPDATE students SET department_id=2 WHERE student_id=5;

-- Introduce Error

INSERT INTO department_transfer_log(student_id,old_department,new_department) VALUES (9999,1,9999);

ROLLBACK;

-- TASK 47- SAVEPOINT Demonstration:

START TRANSACTION;

INSERT INTO enrollments(student_id,course_id,enrollment_date,grade) VALUES (9,2,'2024-07-01',NULL);

SAVEPOINT First_Insert;

-- Deliberately duplicate enrollment

INSERT INTO enrollments(student_id,course_id,enrollment_date,grade) VALUES (9,2,'2024-07-01',NULL);

ROLLBACK TO First_Insert;

COMMIT;

-- Verification Queries

SELECT * FROM department_transfer_log;

SELECT * FROM enrollments ORDER BY enrollment_id;
