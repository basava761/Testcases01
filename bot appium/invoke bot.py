from appium import webdriver

desired_cap={
  "platformName": "Android",
  "platformVersion": "9.0",
  "deviceName": "MIKO",
  "udid": "192.168.1.33:5555",
  "automationName": "UiAutomator2"
}
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

