import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# -----------------------------
# Base URL Fixture
# -----------------------------
@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# -----------------------------
# Driver Fixture
# -----------------------------
@pytest.fixture(scope="function")
def driver(request):

    options = Options()

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    request.node.driver = driver

    yield driver

    driver.quit()


# -----------------------------
# Screenshot on Failure
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            filename = f"screenshots/{item.name}_failure.png"

            driver.save_screenshot(filename)
