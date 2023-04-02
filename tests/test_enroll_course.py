import time

from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_add_to_cart(self):
        #print(self.driver.page_source)
        #time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Browse']").click()
        self.driver.implicitly_wait(30)
        if self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").is_displayed():
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Search']").click()
        # scroll until music category is visible
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Music")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        # above script belongs to mobile commands-> to execute mobile command we required dict
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Music']").click()
        size = self.driver.get_window_size()
        x1 = size['width'] * (50 / 100)
        y1 = size['width'] * (60 / 100)
        x2 = size['width'] * (50 / 100)
        y2 = size['width'] * (40 / 100)  # diff b/w y1 & y2 will be 50
        self.driver.implicitly_wait(0)
        # swipe until Popular topics present in screen
        while len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Popular topics']")) == 0:
            self.driver.swipe(x1, y1, x2, y2, 1000)
        # scroll until Guitar is visible under Popular Topics
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Guitar")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Guitar']").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Complete Guitar Lessons System - Beginner to Advanced']").click()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Add to cart']").click()
        time.sleep(5)

