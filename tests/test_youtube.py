import time
import json
import sys
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.youtube_page import YouTubePage

with open("./config/youtubeConfig.json", "r") as file:
    config = json.load(file)

options = UiAutomator2Options()
options.platform_name = config["platform_name"]
options.device_name = config["device_name"]
options.app_package = config["app_package"]
options.app_activity = config["app_activity"]
options.no_reset = True
options.full_reset = False

driver = webdriver.Remote(config["url"], options=options)
driver.implicitly_wait(10)

print("YouTube 앱 실행됨")

youtube_page = YouTubePage(driver)

youtube_page.allowPermission()
youtube_page.click_shorts_tab()
youtube_page.click_go_to_channel()
youtube_page.click_search_button()
youtube_page.search_channel("blackpink")
youtube_page.click_view_channel()
youtube_page.click_channel_tab("Videos")
youtube_page.click_first_video()

# 종료
time.sleep(5)
driver.quit()
