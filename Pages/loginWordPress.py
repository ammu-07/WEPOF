class LoginWordPress():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "user_login"
        self.password_textbox_id = "user_pass"
        self.submit_button_id = "wp-submit"
        self.reset_to_defaults_button_name = "reset_fields"

    def login_wordpress_dashboard(self, username, password):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        self.driver.find_element_by_id(self.submit_button_id).click()

        self.driver.get("https://test1.floopbox.com/wp-admin/edit.php?post_type=product&page=thwepof_extra_product_options")
        self.driver.find_element_by_name(self.reset_to_defaults_button_name).click()
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()










