class LoginDrawer():
    def __init__(self, driver):
        self.driver = driver

        self.loginLayer_tab_id = "login_Layer"
        self.username_textbox_css = "form[name=login-form] input[type=text]"
        self.password_textbox_css = "form[name=login-form] input[type=password]"
        self.login_button_css = "form[name=login-form] button[type=submit]"

    def click_loginLayer_tab(self):
        self.driver.find_element_by_id(self.loginLayer_tab_id).click()

    def enter_username(self, username):
        self.driver.find_element_by_css_selector(self.username_textbox_css).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.password_textbox_css).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_css_selector(self.login_button_css).click()
