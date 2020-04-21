class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.loginLayer_tab_id = "login_Layer"
        self.username_textbox_id = "usernameField"
        self.password_textbox_id = "passwordField"
        self.login_button_xpath = "//button[@type='submit'][1]"

    def click_loginLayer_tab(self):
        self.driver.find_element_by_id(self.loginLayer_tab_id).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
