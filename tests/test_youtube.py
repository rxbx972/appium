from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# 파일 경로 지정
with open("./config/youtubeConfig.json", "r") as file:
    config = json.load(file)

# Appium 설정
options = UiAutomator2Options()
options.platform_name = config["platform_name"]
options.device_name = config["device_name"]
options.app_package = config["app_package"]
options.app_activity = config["app_activity"]
options.no_reset = True
options.full_reset = False

# Appium 서버 연결
driver = webdriver.Remote(config["url"], options=options)

# 앱이 실행될 때까지 대기
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
print("Youtube 앱 실행")

# 1) Shorts 탭 클릭
shortsTab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shorts")
shortsTab.click()

# 2) Go to channel 버튼 클릭
goToChannelButton = driver.find_element(
    by=AppiumBy.ACCESSIBILITY_ID, value="Go to channel"
)
goToChannelButton.click()

# 3) Search 버튼 클릭
searchButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
searchButton.click()

# 4) 검색창에 "blackpink" 입력 후 엔터 
searchBox = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text"
)
searchBox.send_keys("blackpink")
driver.press_keycode(66)

# 5) 검색결과 노출될 때까지 대기
result_goToChannelButton = wait.until(
    EC.presence_of_element_located(by=AppiumBy.ACCESSIBILITY_ID, value="Go to channel")
)
# driver.assert_extension_exists
print("검색결과 노출")

# 6) 몇 초 대기 후 종료
time.sleep(5)
driver.quit()
