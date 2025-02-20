import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

import uiautomator2 as u2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app='/Users/jiyeon/Desktop/app.apk'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()

    @classmethod
    def setUpClass(cls):  # 클래스 전체에 대한 초기 설정
        cls.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    @classmethod
    def tearDownClass(cls):  # 클래스의 모든 테스트가 실행된 후 마지막에 수행
        if cls.driver:
            cls.driver.quit()

    ## button_1을 클릭하면 버튼 문구 변경
    def test_1_button_1(self) -> None:
        element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='button_1')
        element.click()

        # 요소가 화면에 보이는 상태가 될 때까지 기다림
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'touch!'))
        )

    ## button_2 클릭
    def test_2_button_2(self) -> None:
        element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='button_2')
        element.click()

    ## Text 입력
    def test_3_text_input(self) -> None:
        element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
        element.click()
        element.send_keys("Hello, world!")
        time.sleep(1)
        

    ## 체크박스를 체크하면, 우측의 문구 변경
    def test_4_checkbox(self) -> None:
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'unchecked'))
        )

        element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckBox')
        element.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'check'))
        )

    ## 토글 버튼 동작
    def test_5_toggle(self) -> None:
        element = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Switch')
        element.click()

    ## 아래로 스크롤 할 경우 button_3 버튼 존재
    def test_6_scroll_down(self) -> None:
        element = None
        while element is None:
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'button_3')
            except:
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()')
                
        element.click()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()

# https://appium.io/docs/en/2.4/quickstart/test-py/