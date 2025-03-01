# Appium(python)

## 테스트 환경
- macOS 13.7.2
- Android 15.0

## 테스트 환경 준비 

1. npm 설치
```
brew install node
```

2. pip 설치
```
brew install python
```

3. Appium 설치
```
npm install -g appium
```

4. `requirements.txt` 파일을 통해 의존성 설치
```
pip install -r requirements.txt
```

5. Android 디바이스 준비

6. `./config/{config}.json` 파일 준비 (아래는 예시)
```
{
    "url": "http://localhost:4723/wd/hub",
    "platform_name": "Android",
    "device_name": "emulator-5554",
    "app_package": "com.google.android.youtube",
    "app_activity": "com.google.android.youtube.app.honeycomb.Shell$HomeActivity"
}
```

## 테스트 실행
1. Appium 서버 실행
```
appium
```

2. 테스트 파일 실행
```
python ./tests/{test}.py
```