# V-Model Analysis – Hands-On 2

## Task 1: V-Model Mapping

### 1. V-Model Diagram

```
               SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)

Requirements Analysis
        │
        │
System Design
        │
        │
Architecture Design
        │
        │
Module Design
        │
        │
      Coding
        ▲
        │
Unit Testing
        │
Integration Testing
        │
System Testing
        │
Acceptance Testing

        TESTING LIFE CYCLE (TDLC)
```

---

## 2. SDLC ↔ TDLC Phase Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements Analysis | Acceptance Testing | Acceptance Test Plan, Requirement Traceability Matrix (RTM) |
| System Design | System Testing | System Test Plan, System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan, Interface Test Cases |
| Module Design | Unit Testing | Unit Test Cases, Unit Test Plan |
| Coding | Test Execution | Executable Code |

---

## 3. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**

- Module is developed.
- Source code is available.
- Unit test cases are prepared.

**Exit Criteria**

- All unit tests executed.
- All critical defects fixed.
- Code coverage achieved.

---

### Integration Testing

**Entry Criteria**

- Unit testing completed.
- Integrated modules available.
- Integration test cases prepared.

**Exit Criteria**

- Interfaces tested successfully.
- No critical integration defects.
- Test report completed.

---

### System Testing

**Entry Criteria**

- Integrated application available.
- System test cases approved.
- Test environment ready.

**Exit Criteria**

- All system test cases executed.
- High and Critical defects fixed.
- Test summary report prepared.

---

### Acceptance Testing

**Entry Criteria**

- System testing completed.
- Application ready for customer validation.
- Acceptance test scenarios prepared.

**Exit Criteria**

- Customer approves application.
- All acceptance criteria satisfied.
- Product ready for deployment.

---

## 4. Early QA Engagement Points

### Requirements Review

QA reviews requirements to:

- Identify ambiguities.
- Ensure requirements are testable.
- Prepare acceptance criteria.

---

### Design Review

QA reviews architecture and design to:

- Identify integration risks.
- Plan integration testing.
- Prepare test strategy before coding begins.

---

# Task 2: Agile QA and Shift-Left Testing

## 5. Problems in Waterfall Testing

### Problem 1

Defects are discovered very late, making them expensive to fix.

---

### Problem 2

Requirements misunderstandings are identified only after development is completed.

---

### Problem 3

Testing delays product release because all testing happens after coding.

---

## 6. QA Role in Agile Ceremonies

### Sprint Planning

- Review user stories.
- Define acceptance criteria.
- Estimate testing effort.

---

### Daily Standup

- Report testing progress.
- Discuss blockers.
- Coordinate with developers.

---

### Sprint Review

- Validate completed features.
- Demonstrate functionality.
- Confirm acceptance criteria are met.

---

### Retrospective

- Discuss testing improvements.
- Identify process issues.
- Suggest automation improvements.

---

## 7. Shift-Left Practices

### A. Review Requirements for Testability

QA reviews requirements before development begins to ensure they are complete, clear, and testable.

---

### B. Write Test Cases Before Coding (TDD/BDD)

QA prepares test scenarios before developers write code so expected behavior is clearly defined.

---

### C. Static Code Analysis

Developers use tools to detect coding issues before executing the application.

Examples:

- Pylint
- SonarQube
- Flake8

---

### D. API Contract Testing

API request and response formats are validated before frontend and backend integration.

Example:

Verify that the `POST /api/courses/` endpoint returns the expected JSON structure.

---

## 8. Acceptance Criteria (Gherkin)

### Scenario 1 – Happy Path

```gherkin
Given the college admin is logged in
When the admin enters a unique course code and valid course details
And clicks Create Course
Then the course should be created successfully
And the API should return HTTP 201 Created
```

---

### Scenario 2 – Duplicate Course Code

```gherkin
Given a course with code "CS101" already exists
When the admin attempts to create another course with code "CS101"
Then the API should reject the request
And return HTTP 409 Conflict
And display "Course code already exists"
```

---

### Scenario 3 – Missing Required Fields

```gherkin
Given the admin is on the Create Course page
When the admin submits the form without entering the course name
Then the API should return HTTP 400 Bad Request
And display "Course name is required"
```

---

# Conclusion

This hands-on covered:

- SDLC Phases
- TDLC Phases
- V-Model Mapping
- Test Artifacts
- Entry Criteria
- Exit Criteria
- Agile QA Integration
- Shift-Left Testing
- Waterfall vs Agile
- Acceptance Criteria using Gherkin
- QA involvement throughout the software development lifecycle
