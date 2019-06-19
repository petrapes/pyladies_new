from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from locators import Locators
from LoginPage import Page

class HomePage(Page):

    def __init__(self, driver):
        self.driver = driver

        self.follow_button_xpath = Locators.follow_button_xpath
        self.following_button_xpath = Locators.following_button_xpath
        self.end_following_confirm_xpath = Locators.end_following_confirm_xpath

    def follow_with_username(self, username):
        try:
            self.push(self.follow_button_xpath)
        except NoSuchElementException:
            print("You are already following this user")

    def unfollow_with_username(self, username):
        try:
            self.push(self.following_button_xpath)
            self.push(self.end_following_confirm_xpath)
        except NoSuchElementException:
            print("You are not following this user")
