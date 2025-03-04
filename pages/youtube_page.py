from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YouTubePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def allowPermission(self):
        self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()

    def click_shorts_tab(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shorts").click()

    def click_go_to_channel(self):
        self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Go to channel"
        ).click()

    def click_search_button(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search").click()

    def search_channel(self, query):
        search_box = self.driver.find_element(
            by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text"
        )
        search_box.send_keys(query)
        self.driver.press_keycode(66)

    def click_view_channel(self):
        element = self.wait.until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    "//android.view.ViewGroup[@content-desc='View Channel']",
                )
            )
        )
        element.click()

    def click_channel_tab(self, tab):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=tab).click()

    def click_first_video(self):
        self.driver.find_element(
            AppiumBy.ID, "com.google.android.youtube:id/results"
        ).find_element(
            AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc][1]"
        ).click()

    def share_video(self):
        shareButton = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Share"))
        )
        shareButton.click()
        copyLinkButton = self.wait.until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/bottom_sheet_list']/android.view.ViewGroup/android.view.ViewGroup[2]",
                )
            )
        )
        copyLinkButton.click()

