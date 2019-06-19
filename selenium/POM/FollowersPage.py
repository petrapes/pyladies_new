from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from LoginPage import Page
from locators import Locators

class FollowersPage(Page):

    def __init__(self, driver):
        self.driver = driver

        self.followers_link_xpath = Locators.followers_link_xpath

    def get_user_followers(self, username, max):
        self.push("//ul[contains(@class,'k9GMp')]//li[2]//a[1]")
        followers_list = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        number_of_followersInList = len(followers_list.find_elements_by_css_selector('li'))
    
        followers_list.click()
        actionChain = webdriver.ActionChains(self.driver)
        
        while (number_of_followers_in_list < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            number_of_followersInList = len(followers_list.find_elements_by_css_selector('li'))
            print(number_of_followersInList)
        
        followers = []
        for user in followers_list.find_elements_by_css_selector('li'):
            user_link = user.find_element_by_css_selector('a').get_attribute('href')
            print(user_link)
            followers.append(user_link)
            if (len(followers) == max):
                break
        return followers