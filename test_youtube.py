import unittest
import uiautomator2 as u2

from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

appium_server_url = "http://127.0.0.1:4723/wd/hub"

capabilities = dict(
    platformName='Android',
    automationName='Appium',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings'
)

class SampleTest(unittest.TestCase):

    # 테스트 실행 전 수행해야하는 코드 작성
    def setUp(self):
        self.driver = webdriver.Remote(
            appium_server_url,
            # capabilities
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

    def test_case_1(self):
        driver = self.driver
        print("hello")
        # wait = WebDriverWait(driver, 20)

        # element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Media')
        # element.click()

        # el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        # el.click()

        # el1 = wait.until(EC.element_to_be_clickable((By.ID, 'com.kakaogame.sample:id/login_ui_button')))
        # el1.click()

        # el2 = driver.find_element(by=AppiumBy.ID, value="com.kakaogame.sample:id/kakao_game_login_idp_item")
        # el2.click()
        # sleep(5)

        # # you could see the failure.
        # idpCode = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ListView/android.widget.FrameLayout[4]/android.widget.TextView")
        # self.assertEqual('iPad', idpCode.get_attribute('text'))
        # sleep(5)

        # el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ListView/android.widget.FrameLayout[6]/android.widget.Button")
        # el3.click()
        # sleep(5)

        # el4 = driver.find_element(by=AppiumBy.ID, value="com.kakaogame.sample:id/kakao_game_sdk_logout_btn_ok")
        # el4.click()
        # sleep(10)

    # 테스트 종료 후 수행해야하는 코드 작성
    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# https://appium.io/docs/en/2.4/quickstart/test-py/
