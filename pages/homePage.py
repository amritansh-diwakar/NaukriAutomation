class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.profileSection_card_css = "div[class='popout profile-section card']"

    def check_profileSection_card(self):
        self.driver.find_element_by_css_selector(self.profileSection_card_css).is_displayed()
