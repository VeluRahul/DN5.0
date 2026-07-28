# QA Concepts & Functional Testing – Hands-On 1

## Task 1: Map Testing Types to a Real System

### 1. Test Levels

### Unit Testing
**Description:**
Test a single function independently.

**Example:**
Test the `create_course()` function to verify it creates a course object when valid data is provided.

**Type:** Functional Testing

---

### Integration Testing
**Description:**
Test interaction between multiple components.

**Example:**
Verify that the `POST /api/courses/` API correctly stores the course in the database.

**Type:** Functional Testing

---

### System Testing
**Description:**
Test the complete application.

**Example:**
A user sends a POST request to create a course, the API stores it in the database, and a GET request retrieves the same course.

**Type:** Functional Testing

---

### User Acceptance Testing (UAT)

**Description:**
Testing performed by the end user.

**Example:**
A college administrator successfully creates, updates, views, and deletes courses using the application.

**Type:** Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing

Checks whether the system behaves according to business requirements.

Examples

- Login
- Create Course
- Delete Course
- Update Course

---

### Non-Functional Testing

Checks how well the application performs.

Example

**Performance Testing**

Verify that the Course API can process 1000 requests within one minute without crashing.

---

## 3. Black-Box Testing vs White-Box Testing

### Black-Box Testing

- Tester does not know the source code.
- Focuses on inputs and outputs.
- Tests functionality.

Performed by:

- QA Engineers
- Testers

---

### White-Box Testing

- Tester has access to the source code.
- Tests logic, conditions, loops and code paths.

Performed by:

- Developers

---

## 4. Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create course with valid data | API is running | Send POST request with valid name, code and credits | Course created successfully with HTTP 201 | | |
| TC002 | Create duplicate course | Course already exists | Send POST request using existing course code | HTTP 409 Conflict returned | | |
| TC003 | Missing required fields | API is running | Send POST request without course name | HTTP 400 Bad Request returned | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
  ↓
Assigned
  ↓
Open
  ↓
Fixed
  ↓
Retest
  ↓
Verified
  ↓
Closed
```

### Rejected

The defect is rejected because

- Cannot reproduce
- Not a bug
- Works as designed
- Duplicate defect

### Deferred

The defect is postponed to a future release because

- Low priority
- Time constraints
- Business decision

---

## 6. Severity and Priority Classification

### Bug A

**Issue**

POST /api/courses/ returns HTTP 500 for every request.

Severity

**Critical**

Priority

**P1**

Reason

The application is unusable because course creation completely fails.

---

### Bug B

**Issue**

Course names longer than 150 characters are silently truncated.

Severity

**Medium**

Priority

**P3**

Reason

The application works but data integrity is affected.

---

### Bug C

**Issue**

Swagger documentation contains a spelling mistake.

Severity

**Low**

Priority

**P4**

Reason

Only documentation is affected.

---

### Bug D

**Issue**

Login sometimes returns HTTP 401 even with correct credentials.

Severity

**High**

Priority

**P1**

Reason

Users cannot reliably log in. Since the issue is intermittent, it is difficult to reproduce and impacts user experience significantly.

---

## 7. Defect Report

### Defect ID

BUG-001

---

### Title

POST /api/courses/ returns HTTP 500 Internal Server Error

---

### Environment

Windows 11

Python 3.12

FastAPI

Chrome Browser

---

### Build Version

Version 1.0

---

### Severity

Critical

---

### Priority

P1

---

### Steps to Reproduce

1. Start the Course Management API.
2. Open Postman.
3. Send a POST request to `/api/courses/`.
4. Provide valid JSON data.
5. Click Send.

---

### Expected Result

Course should be created successfully.

HTTP Status: **201 Created**

---

### Actual Result

API returns

HTTP Status:

**500 Internal Server Error**

No course is created.

---

### Attachments

Screenshot of 500 Internal Server Error.

---

## 8. Severity vs Priority

### Severity

Severity indicates how much the defect affects the application.

Example:

Database corruption is **High Severity**.

---

### Priority

Priority indicates how urgently the defect should be fixed.

Example:

A spelling mistake on the CEO's dashboard has **Low Severity** because it does not affect functionality, but **High Priority** because management wants it fixed before an important presentation.

---

## Conclusion

This hands-on demonstrated:

- Unit Testing
- Integration Testing
- System Testing
- User Acceptance Testing
- Functional Testing
- Non-Functional Testing
- Black-Box Testing
- White-Box Testing
- Defect Lifecycle
- Severity vs Priority
- Test Case Writing
- Defect Reporting
