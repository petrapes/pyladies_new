import unittest
import HtmlTestRunner
from selenium import webdriver
import user_data
import configuration_file
from LoginPage import LoginPage
from HomePage import HomePage
from locators import Locators
from FollowersPage import FollowersPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", "cs")
        firefox_profile.update_preferences()
        self.driver = webdriver.Firefox(
                firefox_profile = firefox_profile, 
                executable_path = configuration_file.firefox_executable_path
        )
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def test_1login_and_logout(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        driver.find_element_by_xpath(Locators.signin_button_xpath).click()

        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        login.logout()
    
    def test_2follow_user(self):
        driver = self.driver
        username = "transformers_42"
        driver.get("https://www.instagram.com/" + username + "/")
        
        driver.find_element_by_xpath(Locators.again_login_button_xpath).click()
        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        homepage = HomePage(driver)
        homepage.follow_with_username(username)
        self.assertTrue(self.driver.find_element_by_xpath("//button[contains(text(),'Sleduji')]")) 

    def test_3unfollow_user(self):
        driver = self.driver
        username = "transformers_42"
        driver.get("https://www.instagram.com/" + username + "/")
        
        driver.find_element_by_xpath(Locators.again_login_button_xpath).click()
        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        homepage = HomePage(driver)
        homepage.unfollow_with_username(username)
        self.assertTrue(self.driver.find_element_by_xpath("//button[contains(text(),'Sledování')]"))
    
    def test_4get_user_followers(self):
        driver = self.driver
        username = "transformers_42"
        driver.get("https://www.instagram.com/" + username + "/")

        driver.find_element_by_xpath(Locators.again_login_button_xpath).click()
        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        followers = FollowersPage (driver)
        followers.get_user_followers(username, 50)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=(configuration_file.html_report_executable_path)))

