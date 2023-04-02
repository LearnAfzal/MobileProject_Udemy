import pytest
from appium import webdriver
from utilities import read_utils


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic=read_utils.get_dic_from_json("../test_data/config.json")

        if json_dic["device"]=="local":
            des_cap = {
                "platformName": "android",
                "deviceName": "moto",
                "app": r"C:\Users\153192\OneDrive - Arrow Electronics, Inc\Desktop\Python Training\com.udemy.android_2023-03-16.apk"
                #"appPackage": "com.google.android.youtube",
                #"appActivity": "com.google.android.libraries.onegoogle.accountmanagement",
                #"noReset": True,
                # "appium:avd":"Pixel_4_API_33"
            }
            self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap)

        else:
            des_cap = {
                "app": "bs://aa104de2e2d069e729c3efae598d5a523082d186",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "dinakaranbalaji1",
                    "accessKey": "6yXRE4nK1fyvTHWA2kPD"
                }
            }
            self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)

        #self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()