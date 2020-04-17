from appium import webdriver
from time import sleep

desired_caps = {
    'appPackage': 'com.jingdong.app.mall',
    'platformName': 'Android',
    'deviceName': '87b0e395',
    'appActivity': 'com.jingdong.app.mall.main.MainActivity',
    'noReset': "True"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(5)
icons = driver.find_elements_by_id('com.jingdong.app.mall:id/gw')
icons[6].click()
sleep(5)
sign_btn = driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"签到领京豆")]')
sign_btn.click()
sleep(5)
back_btn = driver.find_element_by_xpath('//android.view.ViewGroup[contains(@index,"2")]')
back_btn.click()
#driver.quit()