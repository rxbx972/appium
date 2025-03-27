import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class YouTubePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_back(self):
        self.driver.press_keycode(4)

    def allowPermission(self):
        self.driver.find_element(
            by=AppiumBy.ID,
            value="com.android.permissioncontroller:id/permission_allow_button",
        ).click()

    def click_tab(self, tab):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=tab).click()

    def click_go_to_channel(self):
        self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Go to channel"
        ).click()

    def click_search_button(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search").click()

    def search_channel(self, query):
        self.driver.find_element(
            by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text"
        ).send_keys(query)
        self.driver.press_keycode(66)

    def click_view_channel(self):
        time.sleep(1)
        viewChannelButton = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "View Channel"))
        )
        viewChannelButton.click()

    def click_channel_tab(self, tab):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=tab).click()

    def click_first_video(self):
        self.driver.find_element(
            AppiumBy.XPATH, "//*[contains(@content-desc, 'play video')][1]"
        ).click()

    def share_video(self):
        time.sleep(2)
        try:
            shareButton = self.wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Share"))
            )
            shareButton.click()
        except TimeoutException:
            adSkipButton = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ID, "com.google.android.youtube:id/skip_ad_button")
                )
            )
            adSkipButton.click()

            shareButton = self.wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Share"))
            )
            shareButton.click()
        finally:
            copyLinkButton = self.wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.XPATH,
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/bottom_sheet_list']/android.view.ViewGroup/android.view.ViewGroup[2]",
                    )
                )
            )
            copyLinkButton.click()

    def close_miniplayer(self):
        self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Close miniplayer"
        ).click()
