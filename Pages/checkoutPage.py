import re

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.place_order_button_by_name = "//*[@id=\"place_order\"]"
        self.field_title_label_by_display_text = "Text 01:"
        self.field_value_label_by_display_text = "field_value"


    def checkout_page(self, field_name, field_value):

        try:
            if (field_value in self.driver.page_source):
                return field_value

        except ValueError:
            print("Field not found")
            self.driver.save_screenshot("/Users/ammuprakash/Desktop/WEPOF/Screenshots/product_page.png")
            self.driver.find_element_by_xpath(self.place_order_button_by_name).click()