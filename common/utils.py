from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# 파일 경로 지정
with open('config/youtubeConfig.json', 'r') as file:
    config = json.load(file)

# 앱을 종료하고 다시 시작합니다.
def restart_app(driver):
    driver.terminate_app(config['app_package'])
    driver.activate_app(config['app_package'])