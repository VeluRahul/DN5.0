import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# ===================================================
# Task 42 & 45
# Parameterized Simple Form Demo
# ===================================================

@pytest.mark.parametrize(

    "message",

    [

        "Hello",

        "Selenium Automation",

        "12345"

    ]

)

def test_simple_form_submission(

    driver,

    base_url,

    message

):

    driver.get(base_url)

    driver.find_element(

        By.LINK_TEXT,

        "Simple Form Demo"

    ).click()

    textbox = driver.find_element(

        By.ID,

        "user-message"

    )

    textbox.clear()

    textbox.send_keys(message)

    driver.find_element(

        By.ID,

        "showInput"

    ).click()

    output = WebDriverWait(driver,10).until(

        EC.visibility_of_element_located(

            (

                By.ID,

                "message"

            )

        )

    )

    assert output.text == message


# ===================================================
# Task 43
# Checkbox Demo
# ===================================================

def test_checkbox_demo(

    driver,

    base_url

):

    driver.get(base_url)

    driver.find_element(

        By.LINK_TEXT,

        "Checkbox Demo"

    ).click()

    checkbox = driver.find_element(

        By.ID,

        "isAgeSelected"

    )

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()


# ===================================================
# Task 49
# Dropdown Demo
# ===================================================

def test_dropdown_selection(

    driver,

    base_url

):

    driver.get(base_url)

    driver.find_element(

        By.LINK_TEXT,

        "Select Dropdown List"

    ).click()

    dropdown = Select(

        driver.find_element(

            By.ID,

            "select-demo"

        )

    )

    dropdown.select_by_visible_text(

        "Wednesday"

    )

    selected = dropdown.first_selected_option.text

    assert selected == "Wednesday"
