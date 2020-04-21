import time
import os
from pathlib import Path
from selenium import webdriver
import unittest
import HtmlTestRunner
from utilities import Variables, ResumeHandler, WebDriverUtil
from pages.loginDrawer import LoginDrawer
from pages.homePage import HomePage
from pages.profilePage import ProfilePage


class UpdateResume(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        if Variables.browser == 'chrome':
            cls.driver = webdriver.Chrome(executable_path="C:/Drivers/Webdrivers/chromedriver.exe")
        else:
            cls.driver = webdriver.Firefox(executable_path=r'C:/Drivers/Webdrivers/geckodriver.exe')
        cls.driver.set_page_load_timeout(10)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get(Variables.naukri_homepage_url)
        WebDriverUtil.close_all_popup_windows(driver)

        login_drawer = LoginDrawer(driver)
        login_drawer.click_loginLayer_tab()
        login_drawer.enter_username(Variables.naukri_email_id)
        login_drawer.enter_password(Variables.naukri_password)
        login_drawer.click_login_button()

        home_page = HomePage(driver)
        home_page.check_profileSection_card()

    def test_upload_resume(self):
        self.driver.get(Variables.naukri_profile_url)
        resources_resume_pdf_filepath = ResumeHandler.get_latest_resume()
        profile_page = ProfilePage(self.driver)
        profile_page.upload_resume(resources_resume_pdf_filepath)
        self.assertEqual(profile_page.get_success_message(), 'Success')

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.path.join(Path(__file__).parent.parent, "reports")))
