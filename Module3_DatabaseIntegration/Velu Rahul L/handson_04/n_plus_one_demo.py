import mysql.connector
import time

# -------------------------------------------------------
# Database Connection
# -------------------------------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = connection.cursor()

# =======================================================
# Task 56 : N+1 Query Problem
# =======================================================

print("----- N+1 Query Problem -----")

query_count = 0

start_time = time.time()

# First Query
cursor.execute("SELECT * FROM enrollments")
query_count += 1

enrollments = cursor.fetchall()

for enrollment in enrollments:

    student_id = enrollment[1]

    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    query_count += 1

    student = cursor.fetchone()

    print(student)

end_time = time.time()

print("\nQueries Executed :", query_count)
print("Execution Time :", end_time - start_time, "seconds")

# =======================================================
# Task 57 : Optimized JOIN Query
# =======================================================

print("\n----- Optimized JOIN Query -----")

query_count = 0

start_time = time.time()

cursor.execute("""

SELECT
    s.first_name,
    s.last_name,
    c.course_name,
    e.grade

FROM enrollments e

JOIN students s
ON e.student_id = s.student_id

JOIN courses c
ON e.course_id = c.course_id

""")

query_count += 1

records = cursor.fetchall()

for row in records:
    print(row)

end_time = time.time()

print("\nQueries Executed :", query_count)
print("Execution Time :", end_time - start_time, "seconds")

# =======================================================
# Task 58 : Comparison
# =======================================================

print("\n----- Comparison -----")

print("N+1 Version : Multiple Queries Executed")

print("JOIN Version : Single Query Executed")

print("JOIN is much faster and reduces database round trips.")

# =======================================================
# Task 59 : Documentation
# =======================================================

"""
Explanation

N+1 Problem

1 query is executed to fetch all enrollments.

Then,

1 additional query is executed for every enrollment.

If there are

10,000 enrollments

Total Queries

1 + 10000

= 10001 Queries

Using JOIN

Only ONE query is executed.

JOIN is the recommended solution.

ORMs solve this using

select_related()

prefetch_related()

joinedload()

instead of lazy loading.
"""

# -------------------------------------------------------
# Close Connection
# -------------------------------------------------------

cursor.close()
connection.close()
