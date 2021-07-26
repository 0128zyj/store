'''
    python自动化刷抖音
'''

from appium  import  webdriver
import  time

from appium.webdriver.common.touch_action import TouchAction

server = "http://localhost:4723/wd/hub"
param = {
			  "deviceName": "ZHLVPRTGZSRCLNMZ",
			  "platformName": "Android",
			  "platformVersion": "9",
			  "appPackage": "com.ss.android.ugc.aweme",
			  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
# 启动这个软件
driver = webdriver.Remote(server,param)


# 自己写刷抖音
while True:
	TouchAction(driver)   .press(x=479, y=1935)   .move_to(x=526, y=333)   .release()   .perform()
	time.sleep(12)

# driver.quit()






















