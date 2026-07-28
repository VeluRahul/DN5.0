"""
===========================================================
Hands-On 4
Selenium WebDriver Setup, Browser Drivers & Basic Commands
===========================================================

Selenium Components

1. WebDriver
- Selenium WebDriver is the browser automation API.
- It communicates with browser drivers like ChromeDriver
  using the W3C WebDriver Protocol.
- It allows automation of browser actions such as clicking,
  typing, navigating, and retrieving page information.

2. Selenium Grid
- Selenium Grid allows tests to run on multiple machines,
  operating systems, and browsers simultaneously.
- It supports parallel execution, reducing test execution time.

3. Selenium IDE
- Selenium IDE is a browser extension used for
  recording and playback of test cases.
- It is useful for beginners and for generating
  automation scripts quickly.

------------------------------------------------------------

Implicit Wait

driver.implicitly_wait(10)

Implicit Wait tells Selenium to wait for an element
for up to 10 seconds.

Although convenient, implicit waits are generally not
recommended because they apply globally to every element
lookup and can make debugging difficult.

Explicit Waits are preferred because they wait only
for specific conditions and improve reliability.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

import os

# -------------------------------------------------
# Chrome Options
# -------------------------------------------------

options = Options()

# Run browser in headless mode
options.add_argument("--headless=new")

# Optional
options.add_argument("--start-maximized")

# -------------------------------------------------
# Launch Browser
# -------------------------------------------------

driver = webdriver.Chrome(

    service=Service(
        ChromeDriverManager().install()
    ),

    options=options

)

# -------------------------------------------------
# Implicit Wait
# -------------------------------------------------

driver.implicitly_wait(10)

# -------------------------------------------------
# Open Selenium Playground
# -------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Home Page Title:")

print(driver.title)

# -------------------------------------------------
# Navigate to Simple Form Demo
# -------------------------------------------------

driver.find_element(

    By.LINK_TEXT,

    "Simple Form Demo"

).click()

assert "simple-form-demo" in driver.current_url

print("\nCurrent URL:")

print(driver.current_url)

# -------------------------------------------------
# Navigate Back
# -------------------------------------------------

driver.back()

print("\nBack to Home Page")

# -------------------------------------------------
# Open Google in New Tab
# -------------------------------------------------

driver.execute_script(

    'window.open("https://www.google.com");'

)

print("\nWindow Handles:")

print(driver.window_handles)

# -------------------------------------------------
# Switch to Google Tab
# -------------------------------------------------

driver.switch_to.window(

    driver.window_handles[1]

)

print("\nGoogle Title:")

print(driver.title)

# -------------------------------------------------
# Switch Back
# -------------------------------------------------

driver.switch_to.window(

    driver.window_handles[0]

)

# -------------------------------------------------
# Screenshot
# -------------------------------------------------

driver.save_screenshot(

    "playground_screenshot.png"

)

print("\nScreenshot Saved")

print(

    os.path.abspath(

        "playground_screenshot.png"

    )

)

# -------------------------------------------------
# Window Size
# -------------------------------------------------

print("\nOriginal Window Size:")

print(driver.get_window_size())

driver.set_window_size(

    1280,

    800

)

print("\nUpdated Window Size:")

print(driver.get_window_size())

"""
A consistent browser window size is important because
responsive web pages change layout depending on the
screen resolution.

Using a fixed window size ensures reliable and
repeatable Selenium tests.
"""

# -------------------------------------------------
# Close Browser
# -------------------------------------------------

driver.close()

driver.quit()

print("\nExecution Completed Successfully.")
