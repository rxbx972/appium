import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait

#1 기다렸다가 클릭하는 함수 wait_Element / wait_Elements 
def wait_Element(driver, xpath):
    location = xpath

    try:
        element:WebElement = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    except TimeoutException:
        print("Timeout!!!!!!!!!!!!")
        return False

def wait_Elements(driver, xpath):
    location = xpath
    wait_Element(driver, location)
    return driver.find_elements(By.XPATH, location)

#2 appium 세팅
@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='emulator-5554'
    )

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.press_keycode(3)

    yield driver
    driver.quit()

#3 테스트케이스
def test_case_01(driver):
    el = wait_Element(driver, '//android.widget.TextView[@content-desc="YouTube"]')
    # el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="YouTube"]')
    el.click()