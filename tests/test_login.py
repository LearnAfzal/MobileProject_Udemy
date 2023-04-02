import time

from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_invalid_login(self):
        #print(self.driver.page_source)
        #time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Sign In']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in with email']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email']").send_keys("afzal123@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Next']").click()
        signin_user=self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("Enter your password to sign in with")').text
        print(signin_user)
        #assert_that(signin_user).is_equal_to("Enter your password to sign in with afzal123@gmail.com")
        #how to assert a msg which is displayed in 2 lines
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.udemy.android:id/password']").send_keys("afzal123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Sign In']").click()
        error_msg=signin_user=self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("There was a problem logging in")').text
        print(error_msg)
        assert_that(signin_user).is_equal_to("There was a problem logging in. Check your email and password or create an account.")
        time.sleep(2)

    