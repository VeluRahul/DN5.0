-- TASK 1 : Create database

CREATE DATABASE college_db;

USE college_db;

-- CREATE TABLE : departments 

CREATE TABLE departments(department_id INT AUTO_INCREMENT PRIMARY KEY,dept_name VARCHAR(100) NOT NULL,hod_name VARCHAR(100),budget DECIMAL(12,2));

-- CREATE TABLE : students

CREATE TABLE students(student_id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(50) NOT NULL,last_name VARCHAR(50) NOT NULL,email VARCHAR(100) UNIQUE NOT NULL,date_of_birth DATE,department_id INT,enrollment_year INT,FOREIGN KEY (department_id) REFERENCES departments(department_id));

-- CREATE TABLE : courses

CREATE TABLE courses(course_id INT AUTO_INCREMENT PRIMARY KEY,course_name VARCHAR(150) NOT NULL,course_code VARCHAR(20) UNIQUE,credits INT,department_id INT,FOREIGN KEY (department_id)REFERENCES departments(department_id));

-- CREATE TABLE : enrollments

CREATE TABLE enrollment(enrollment_id INT AUTO_INCREMENT PRIMARY KEY,student_id INT,course_id INT,enrollment_date DATE,grade CHAR(2),FOREIGN KEY(student_id)REFERENCES students(student_id),FOREIGN KEY(course_id)REFERENCES courses(course_id));

-- CREATE TABLE : professors

CREATE TABLE professors(professor_id INT AUTO_INCREMENT PRIMARY KEY,prof_name VARCHAR(100) NOT NULL,email VARCHAR(100) UNIQUE,department_id INT,salary DECIMAL(10,2),FOREIGN KEY(department_id)REFERENCES departments(department_id));

-- verify table structure

DESCRIBE departments;

DESCRIBE students;

DESCRIBE courses;

DESCRIBE enrollments;

DESCRIBE professors;

-- TASK 2 : normalisation analysis

-- 1NF
-- Every column stores only one value.
-- Example violation:
-- phone_numbers = '9876543210,9876543222'
-- This is not atomic and violates First Normal Form.

-- 2NF
-- All non-key attributes depend completely on the
-- primary key.
-- Enrollment attributes depend on the enrollment record.
-- There are no partial dependencies.

-- 3NF
-- No transitive dependency exists.
-- Department name is stored only in departments table.
-- Students reference departments using department_id.
-- This avoids redundancy and maintains Third Normal Form.
-- Enrollment contains only enrollment-specific data.

-- TASK 3 : Alter Table

-- Added phone number by using the following query

ALTER TABLE students ADD phone_number VARCHAR(15);

-- Added maximum seats by using the following query

ALTER TABLE courses ADD max_seats INT DEFAULT 60;

-- Add CHECK constraint by using the following query

ALTER TABLE enrollments ADD CONSTRAINT chk_grade CHECK(grade IN ('A','B','C','D','F') OR grade IS NULL);

-- Rename column

ALTER TABLE departments RENAME COLUMN hod_name TO head_of_dept;

-- Drop phone number

ALTER TABLE students DROP COLUMN phone_number;

-- to verify final structure

DESCRIBE departments;

DESCRIBE students;

DESCRIBE courses;

DESCRIBE enrollments;

DESCRIBE professors;
