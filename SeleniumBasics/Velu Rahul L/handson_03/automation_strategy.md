# Automation Strategy – Hands-On 3

## Task 1: Automation Decision and Test Case Selection

### 1. Criteria for Deciding Whether to Automate

#### Criterion 1: Frequency of Execution
Tests that are executed repeatedly should be automated.

**Application to POST /api/courses/**

The endpoint is tested after every code change, making it a good candidate for automation.

---

#### Criterion 2: Regression Testing

Regression tests ensure existing functionality still works after updates.

**Application**

The course creation API is part of the regression suite and should be automated.

---

#### Criterion 3: Stable Functionality

Stable features that rarely change are suitable for automation.

**Application**

The course creation endpoint has fixed functionality and is suitable for automation.

---

#### Criterion 4: Data-Driven Testing

Tests requiring multiple input combinations benefit from automation.

**Application**

Different course names, codes, and credits can be tested automatically using various datasets.

---

#### Criterion 5: Time Saving

Automation saves time for repetitive manual tasks.

**Application**

Instead of manually testing the API after every build, automated tests can execute within seconds.

---

## 2. Manual vs Automated Test Cases

| Test Case | Decision | Justification |
|------------|----------|---------------|
| Regression testing for all CRUD endpoints | Automate | Executed frequently after every code change |
| Exploratory testing of new search feature | Manual | Requires human creativity and observation |
| Performance testing with 100 concurrent users | Automate | Performance tools execute repeated load tests efficiently |
| Login UI testing | Automate | Stable UI functionality and frequent regression testing |
| Verify Swagger documentation | Manual | Documentation requires visual verification and review |
| Smoke testing after deployment | Automate | Quick validation executed after every deployment |

---

## 3. Test Automation ROI

### Definition

Automation ROI (Return on Investment) measures whether the time invested in creating automation is recovered through repeated executions.

---

### Given

Automation Development Time = **4 hours**

Manual Execution Time = **30 minutes = 0.5 hour**

---

### Break-even Calculation

```
4 ÷ 0.5 = 8 runs
```

Automation becomes beneficial after approximately **8 executions**.

---

### Maintenance Overhead

After the 10th execution, maintenance requires 20% of manual execution time.

Manual execution = 30 minutes

Maintenance per run

```
30 × 20%

= 6 minutes
```

Even with maintenance, automation remains significantly more efficient than manual testing for long-term regression testing.

---

## 4. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes in the application.

---

### Example

A Selenium test clicks the Login button before the page finishes loading.

Sometimes it passes.

Sometimes it fails.

---

### Strategies to Prevent Flaky Tests

- Use Explicit Waits instead of Thread.sleep().
- Ensure test data is independent.
- Use stable element locators such as ID instead of XPath whenever possible.

---

# Task 2: Automation Framework Types

## 5. Framework Comparison

### Linear Framework

#### Description

Test scripts are written sequentially without reusable components.

#### Advantage

Easy to understand.

#### Disadvantage

High maintenance.

#### Example

Automating a simple login page.

---

### Modular Framework

#### Description

Application functionality is divided into reusable modules.

#### Advantage

High code reuse.

#### Disadvantage

Requires planning and modular design.

#### Example

Separate Login, Course, and Student modules for the Course Management system.

---

### Data-Driven Framework

#### Description

Test data is stored separately from test scripts.

#### Advantage

Same script can execute multiple datasets.

#### Disadvantage

Managing external data files increases complexity.

#### Example

Testing login using 50 username-password combinations from an Excel sheet.

---

### Keyword-Driven Framework

#### Description

Tests are executed using predefined keywords.

#### Advantage

Non-technical users can create test cases.

#### Disadvantage

Complex framework implementation.

#### Example

Keywords such as Login, ClickButton, VerifyMessage for Course Management.

---

### Hybrid Framework

#### Description

Combines Modular, Data-Driven, and Keyword-Driven approaches.

#### Advantage

Highly reusable, scalable, and maintainable.

#### Disadvantage

Initial setup requires more effort.

#### Example

Enterprise Selenium automation framework for Course Management.

---

## 6. Recommended Framework

### Requirements

- Login testing with 50 users
- Reusable login functionality
- Support technical and non-technical users

### Recommendation

**Hybrid Framework**

Reason:

- Modular design provides reusable login components.
- Data-Driven testing supports multiple login credentials.
- Keyword-Driven testing enables non-technical testers.
- Suitable for large enterprise projects.

---

## 7. Hybrid Framework Folder Structure

```
CourseManagementAutomation/

│

├── config/

│   ├── config.properties

│   └── browser.properties

│

├── testdata/

│   ├── loginData.xlsx

│   ├── courseData.xlsx

│   └── studentData.xlsx

│

├── pages/

│   ├── LoginPage.py

│   ├── DashboardPage.py

│   ├── CoursePage.py

│   └── StudentPage.py

│

├── tests/

│   ├── test_login.py

│   ├── test_courses.py

│   └── test_students.py

│

├── utilities/

│   ├── BrowserUtils.py

│   ├── ExcelUtils.py

│   ├── WaitUtils.py

│   └── ScreenshotUtils.py

│

├── reports/

│

├── screenshots/

│

├── logs/

│

└── requirements.txt
```

---

# Conclusion

This hands-on covered:

- Test Automation Decision Criteria
- Manual vs Automated Testing
- Automation ROI
- Flaky Tests
- Linear Framework
- Modular Framework
- Data-Driven Framework
- Keyword-Driven Framework
- Hybrid Framework
- Framework Selection Strategy
- Hybrid Selenium Project Structure
