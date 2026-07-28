"""
===========================================================
Hands-On 5
Locators & Explicit Waits
===========================================================

Locator Ranking (Most Preferred → Least Preferred)

1. ID
   - Unique
   - Fast
   - Easy to maintain

2. NAME
   - Usually unique
   - Readable

3. CSS Selector
   - Fast
   - Flexible
   - Preferred over XPath

4. Relative XPath
   - Useful when CSS cannot locate an element
   - More readable than absolute XPath

5. Class Name
   - Often shared by multiple elements

6. Absolute XPath
   - Very fragile
   - Breaks when page structure changes
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground")

driver.implicitly_wait(5)

# =====================================================
# Task 32
# Simple Form Demo
# =====================================================

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# By.ID
driver.find_element(By.ID, "user-message")

# By.NAME
driver.find_element(By.NAME, "user-message")

# By.CLASS_NAME
driver.find_element(By.CLASS_NAME, "form-control")

# By.TAG_NAME
driver.find_element(By.TAG_NAME, "input")

# Absolute XPath
driver.find_element(
    By.XPATH,
    "/html/body/div[2]//input"
)

# Relative XPath
driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("All Locator Strategies Successful")

# =====================================================
# Task 33
# CSS Selectors
# =====================================================

driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

driver.find_element(
    By.CSS_SELECTOR,
    "[name='user-message']"
)

driver.find_element(
    By.CSS_SELECTOR,
    "div.col-md-6 input"
)

print("CSS Selectors Successful")

# =====================================================
# Task 34
# Checkbox Demo
# =====================================================

driver.get(
    "https://www.lambdatest.com/selenium-playground/checkbox-demo"
)

label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print(label.text)

labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Checkbox Labels Found:", len(labels))

# =====================================================
# Task 36
# Bootstrap Alerts
# =====================================================

driver.get(
    "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"
)

button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(
        (
            By.ID,
            "autoclosable-btn-success"
        )
    )
)

button.click()

alert = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (
            By.CSS_SELECTOR,
            ".alert-success"
        )
    )
)

assert "successfully" in alert.text.lower()

print(alert.text)

# =====================================================
# Task 37
# sleep vs Explicit Wait
# =====================================================

driver.refresh()

start = time.time()

driver.find_element(
    By.ID,
    "autoclosable-btn-success"
).click()

time.sleep(3)

print("Sleep Time")

print(time.time()-start)

driver.refresh()

start = time.time()

driver.find_element(
    By.ID,
    "autoclosable-btn-success"
).click()

WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (
            By.CSS_SELECTOR,
            ".alert-success"
        )
    )
)

print("Explicit Wait Time")

print(time.time()-start)

"""
Explicit Wait is preferred because it waits only
until the condition is met.

sleep() always waits the full duration,
making tests slower and less reliable.
"""

# =====================================================
# Task 38
# Clickable Wait
# =====================================================

driver.refresh()

button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(
        (
            By.ID,
            "autoclosable-btn-success"
        )
    )
)

button.click()

"""
visibility_of_element_located
--------------------------------

Element exists and is visible.

element_to_be_clickable
--------------------------------

Element is visible AND enabled AND can be clicked.
"""

# =====================================================
# Task 39
# Fluent Wait
# =====================================================

wait = WebDriverWait(

    driver,

    timeout=10,

    poll_frequency=0.5,

    ignored_exceptions=[
        NoSuchElementException
    ]

)

wait.until(

    EC.presence_of_element_located(

        (
            By.CSS_SELECTOR,
            ".alert-success"
        )

    )

)

print("Fluent Wait Successful")

driver.quit()
