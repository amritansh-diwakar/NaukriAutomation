class ProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.attachCv_fileupload_id = "attachCV"
        self.success_message_css = "p[class='head']"

    def upload_resume(self,resume_file):
        self.driver.find_element_by_id(self.attachCv_fileupload_id).send_keys(resume_file)

    def get_success_message(self):
        return self.driver.find_element_by_css_selector(self.success_message_css).text
