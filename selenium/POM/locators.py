class Locators():
    # Login locators
    signin_button_xpath = "//a[contains(text(),'Přihlaste se')]"
    username_textbox_name = "username"
    password_textbox_name = "password"
    login_button_xpath = "//div[contains(text(),'Přihlásit se')]"
    again_login_button_xpath = "//button[contains(text(),'Přihlásit se')]"
    
    # Logout locators
    click_following_xpath = "//button[contains(text(),'Zapnout')]"
    profile_link_xpath = "//span[@class='glyphsSpriteUser__outline__24__grey_9 u-__7']"
    options_link_xpath = "//span[@class='glyphsSpriteSettings__outline__24__grey_9 u-__7']"
    logout_link_xpath = "//button[contains(text(),'Odhlásit se')]"

    # HomePage locators
    follow_button_xpath = "//button[contains(text(),'Sledování')]"
    following_button_xpath = "//button[contains(text(),'Sleduji')]"
    end_following_confirm_xpath = "//button[contains(text(),'Zrušit sledování')]"

    # Followers locators
    followers_link_xpath = "//ul[contains(@class,'k9GMp')]//li[2]//a[1]"