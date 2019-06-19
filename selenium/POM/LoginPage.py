from locators import Locators

class Page():

    def __init__(self, driver):
        self.driver = driver

    def push(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def clean(self, name_of_element):
        self.driver.find_element_by_name(name_of_element).clear()


class LoginPage(Page):

    def __init__(self, driver):
        self.driver = driver
    
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.click_following_xpath = Locators.click_following_xpath
        self.profile_link_xpath = Locators.profile_link_xpath
        self.options_link_xpath = Locators.options_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath

    def enter_username(self, username):
        self.clean(self.username_textbox_name)
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
    
    def enter_password(self, password):
        self.clean(self.password_textbox_name)
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)
    
    def click_login(self):
        self.push(self.login_button_xpath)

    def logout(self):
        self.push(self.click_following_xpath)
        self.push(self.profile_link_xpath)
        self.push(self.options_link_xpath)
        self.push(self.logout_link_xpath)