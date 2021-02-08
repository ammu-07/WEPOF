from selenium.webdriver.support.ui import Select


class AddSelectField():

    def __init__(self, driver):

        self.driver = driver
        self.reset_to_defaults_button_name = "reset_fields"
        self.reset_to_defaults_button_name = "reset_fields"
        self.add_field_button_xpath = "//*[@id=\"thwepof_product_fields\"]/thead/tr[1]/th[1]/button[1]"
        self.field_name_textbox_xpath = "//*[@id=\"thwepof_field_form\"]/div[1]/div/table[1]/tbody/tr[2]/td[3]/input"
        self.field_title_textbox_xpath = "//*[@id=\"thwepof_field_form\"]/div[1]/div/table[2]/tbody/tr[1]/td[3]/input"
        self.field_type_select_xpath = "//*[@id=\"thwepof_field_form\"]/div[1]/div/table[1]/tbody/tr[1]/td[3]/select"
        self.field_options_xpath = "//*[@id=\"thwepof_field_form\"]/div[1]/div/table[2]/tbody/tr[3]/td[3]/input"
        self.create_field_button_xpath = "//*[@id=\"thwepof_field_form_pp\"]/div/div/div/div/div/footer/div/button[1]/span"

    def create_select_field(self, field_type, field_name, field_title, field_options):

        self.driver.find_element_by_name(self.reset_to_defaults_button_name).click()
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

        self.driver.find_element_by_xpath(self.add_field_button_xpath).click()
        self.i_type = Select(self.driver.find_element_by_xpath(self.field_type_select_xpath))
        self.i_type.select_by_value(field_type)
        self.driver.find_element_by_xpath(self.field_name_textbox_xpath).send_keys(field_name)
        self.driver.find_element_by_xpath(self.field_title_textbox_xpath).send_keys(field_title)
        self.driver.find_element_by_xpath(self.field_options_xpath).send_keys(field_options)
        self.driver.find_element_by_xpath(self.create_field_button_xpath).click()