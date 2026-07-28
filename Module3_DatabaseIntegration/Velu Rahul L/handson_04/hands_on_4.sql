-----------------------------------------------------------
-- Task 1 : Baseline Performance
-----------------------------------------------------------

-- 48. View Execution Plan

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-----------------------------------------------------------

-- 49. Identify Table Scan

-- After running the above EXPLAIN command,
-- check the execution plan.

-- Example Observation:

-- MySQL
-- Full Table Scan on students table.

-- PostgreSQL
-- Sequential Scan on students table.

-----------------------------------------------------------

-- 50. Estimated Cost / Rows Examined

-- After executing EXPLAIN,
-- copy the execution plan output below.

-- Example (PostgreSQL)

-- Seq Scan on students
-- Hash Join
-- Nested Loop
--
-- Estimated Cost:
-- 25.40..48.70

-- Example (MySQL)

-- type : ALL
-- rows : 8
-- filtered : 100%

-- Observation:

-- Since the tables currently contain only a few records,
-- the database optimizer prefers a Full Table Scan
-- (MySQL) or Sequential Scan (PostgreSQL) instead of
-- using indexes.

-- As the number of records increases, indexes will
-- significantly improve query performance.

-----------------------------------------------------------
-- Task 2 : Create Indexes
-----------------------------------------------------------

-- 51. Create B-Tree Index on enrollment_year

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

-----------------------------------------------------------

-- 52. Create Composite UNIQUE Index

CREATE UNIQUE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);

-----------------------------------------------------------

-- 53. Create Index on course_code

CREATE INDEX idx_courses_course_code
ON courses(course_code);

-----------------------------------------------------------

-- 54. Run EXPLAIN Again

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Observation:
--
-- Before Index:
-- Full Table Scan / Sequential Scan
--
-- After Index:
-- Index Scan may be used on students table
-- using idx_students_enrollment_year.
--
-- Query execution becomes faster for large tables.

-----------------------------------------------------------

-- 55. Create Partial Index
-----------------------------------------------------------

-- PostgreSQL

CREATE INDEX idx_pending_grades
ON enrollments(student_id)
WHERE grade IS NULL;

-- MySQL Note:
-- Partial indexes using WHERE are NOT supported.
-- If using MySQL, create a normal index instead.

-- MySQL Alternative

CREATE INDEX idx_pending_grades
ON enrollments(student_id);
