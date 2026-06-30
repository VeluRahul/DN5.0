-- TASK 1 : INSERT DATA


-- departments

INSERT INTO departments (dept_name, head_of_dept, budget) VALUES
('Computer Science','Dr. Ramesh Kumar',850000.00),
('Electronics','Dr. Priya Nair',620000.00),
('Mechanical','Dr. Suresh Iyer',540000.00),
('Civil','Dr. Ananya Sharma',430000.00);

SELECT COUNT(*) AS Total_Departments
FROM departments;

-- students

INSERT INTO students
(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Arjun','Mehta','arjun.mehta@college.edu','2003-04-12',1,2022),
('Priya','Suresh','priya.suresh@college.edu','2003-07-25',1,2022),
('Rohan','Verma','rohan.verma@college.edu','2002-11-08',2,2021),
('Sneha','Patel','sneha.patel@college.edu','2004-01-30',3,2023),
('Vikram','Das','vikram.das@college.edu','2003-09-14',1,2022),
('Kavya','Menon','kavya.menon@college.edu','2002-05-17',2,2021),
('Aditya','Singh','aditya.singh@college.edu','2004-03-22',4,2023),
('Deepika','Rao','deepika.rao@college.edu','2003-08-09',1,2022);

-- Two additional students
INSERT INTO students
(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Rahul','Velu','rahul.velu@college.edu','2005-01-22',1,2023),
('Nisha','Kumar','nisha.kumar@college.edu','2004-09-15',2,2022);

SELECT COUNT(*) AS Total_Students
FROM students;

-- courses

INSERT INTO courses
(course_name,course_code,credits,department_id)
VALUES
('Data Structures & Algorithms','CS101',4,1),
('Database Management Systems','CS102',3,1),
('Object Oriented Programming','CS103',4,1),
('Circuit Theory','EC101',3,2),
('Thermodynamics','ME101',3,3);

SELECT COUNT(*) AS Total_Courses
FROM courses;

-- enrollments

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(1,1,'2022-07-01','A'),
(1,2,'2022-07-01','B'),
(2,1,'2022-07-01','B'),
(2,3,'2022-07-01','A'),
(3,4,'2021-07-01','A'),
(4,5,'2023-07-01',NULL),
(5,1,'2022-07-01','C'),
(5,2,'2022-07-01','A'),
(6,4,'2021-07-01','B'),
(7,5,'2023-07-01',NULL),
(8,1,'2022-07-01','A'),
(8,3,'2022-07-01','B');

SELECT COUNT(*) AS Total_Enrollments
FROM enrollments;

-- professors

INSERT INTO professors
(prof_name,email,department_id,salary)
VALUES
('Dr. Anand Krishnan','anand.k@college.edu',1,95000.00),
('Dr. Meena Pillai','meena.p@college.edu',1,88000.00),
('Dr. Sunil Rajan','sunil.r@college.edu',2,82000.00),
('Dr. Latha Gopal','latha.g@college.edu',3,79000.00),
('Dr. Kartik Bose','kartik.b@college.edu',4,76000.00);

SELECT COUNT(*) AS Total_Professors
FROM professors;

-- TASK 17
-- Update Grade :

UPDATE enrollments
SET grade='B'
WHERE student_id=5
AND course_id=1;

SELECT *
FROM enrollments
WHERE student_id=5
AND course_id=1;

-- TASK 18
-- Delete NULL Grades :

SELECT *
FROM enrollments
WHERE grade IS NULL;

DELETE FROM enrollments
WHERE grade IS NULL;

SELECT COUNT(*) AS Remaining_Enrollments
FROM enrollments;

-- TASK 20
-- Students enrolled in 2022 :

SELECT *
FROM students
WHERE enrollment_year=2022
ORDER BY last_name ASC;

-- TASK 21
-- Courses having more than 3 credits :

SELECT *
FROM courses
WHERE credits>3
ORDER BY credits DESC;

-- TASK 22
-- Professors salary between 80000 and 95000 :


SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;

-- TASK 23
-- Email ends with @college.edu :

SELECT *
FROM students
WHERE email LIKE '%@college.edu';

-- TASK 24
-- Students per enrollment year :

SELECT
enrollment_year,
COUNT(*) AS Total_Students
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year;

-- TASK 25
-- Student Name with Department Name :

SELECT
    CONCAT(s.first_name,' ',s.last_name) AS Student_Name,
    d.dept_name AS Department
FROM students s
INNER JOIN departments d
ON s.department_id = d.department_id;

-- TASK 26
-- Enrollment with Student and Course :

SELECT
    CONCAT(s.first_name,' ',s.last_name) AS Student_Name,
    c.course_name,
    e.enrollment_date,
    e.grade
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON e.course_id = c.course_id;

-- TASK 27
-- Students Not Enrolled in Any Course :

SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS Student_Name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

-- TASK 28
-- Course with Number of Students :

SELECT
    c.course_name,
    COUNT(e.student_id) AS Student_Count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id,c.course_name
ORDER BY Student_Count DESC;

-- TASK 29
-- Department with Professors :

SELECT
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
ORDER BY d.dept_name;

-- TASK 30
-- Total Enrollments Per Course :

SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS Enrollment_Count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id,c.course_name
ORDER BY Enrollment_Count DESC;

-- TASK 31
-- Average Salary oer Department :

SELECT
    d.dept_name,
    ROUND(AVG(p.salary),2) AS Average_Salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id,d.dept_name;

-- TASK 32
-- Departments Having Budget greater than 600000 :

SELECT
    dept_name,
    budget
FROM departments
WHERE budget > 600000;

-- TASK 33
-- Grade Distribution for CS101 :

SELECT
    e.grade,
    COUNT(*) AS Grade_Count
FROM enrollments e
INNER JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade;

-- TASK 34
-- Departments Having More Than Two Students :

SELECT
    d.dept_name,
    COUNT(s.student_id) AS Total_Students
FROM departments d
INNER JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id,d.dept_name
HAVING COUNT(s.student_id) > 2;
