from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Appium 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"  
options.app_package = "com.google.android.youtube"
options.app_activity = "com.google.android.youtube.app.honeycomb.Shell$HomeActivity"
options.no_reset = True
options.full_reset = False

# Appium 서버 연결
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

# 앱이 실행될 때까지 대기
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
print("Youtube 앱 실행")

# 1) Shorts 탭 클릭
shortsTab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Shorts')
shortsTab.click()

# 2) Go to channel 버튼 클릭
goToChannelButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Go to channel')
goToChannelButton.click()

# 3) Search 버튼 클릭
searchButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Search')
searchButton.click()

# 검색창에 "Appium Tutorial" 입력 후 검색 수행
searchBox = driver.find_element(by=AppiumBy.ID, value='com.google.android.youtube:id/search_edit_text')
searchBox.send_keys("blackpink") 
driver.press_keycode(66)

# 검색결과 노출될 때까지 대기
result_goToChannelButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Go to channel')
# driver.find_element(by=AppiumBy.XPATH, value=xpath)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

# wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
# element:WebElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
print("검색결과 노출")

# 몇 초 대기 후 종료
time.sleep(5)
driver.quit()
