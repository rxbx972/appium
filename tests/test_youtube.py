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
wait = WebDriverWait(driver, 10)

# 앱이 실행될 때까지 대기
driver.implicitly_wait(10)
print("Youtube 앱 실행")

# 0) 알림 권한 팝업 허용 클릭
# permissionAllowButton = driver.find_element(
#     by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button"
# )
# permissionAllowButton.click()

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

# 5) 검색결과 노출될 때까지 대기, 채널 클릭
result_ViewChannelButton = wait.until(
    EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='View Channel']")
    )
)

result_ViewChannelButton.click()

# 6) 채널 이동 후 비디오 탭 클릭
channel_videoTab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Videos")
# //android.widget.TextView[@resource-id="com.google.android.youtube:id/text" and @text="Videos"]
channel_videoTab.click()

# 7) 비디오 리스트 중 첫번째 비디오 클릭
channel_videoList = driver.find_element(
    AppiumBy.ID, "com.google.android.youtube:id/results"
)
firstVideo = channel_videoList.find_element(
    AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc][1]"
)
firstVideo.click()

# 8) 공유 버튼 클릭, url 복사
shareButton = wait.until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Share"))
)
shareButton.click()
copyLinkButton = wait.until(
    EC.presence_of_element_located(
        (
            AppiumBy.XPATH,
            "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/bottom_sheet_list']/android.view.ViewGroup/android.view.ViewGroup[2]",
        )
    )
)
copyLinkButton.click()

# 9) 몇 초 대기 후 종료
time.sleep(5)
driver.quit()
