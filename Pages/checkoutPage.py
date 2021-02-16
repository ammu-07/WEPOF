import re

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.place_order_button_by_xpath = "//*[@id=\"place_order\"]"
        self.field_title_label_by_display_text = "Text 01:"
        self.field_value_label_by_display_text = "field_value"


    def checkout_page(self, field_value):

        try:
            self.driver.find_element_by_id('dummy_value')
        except:
            print(" ")

        try:
            print("Field successfully displayed at Checkout page")
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(self.place_order_button_by_xpath).click()

        except ValueError:
            print("Field not found")
            self.driver.save_screenshot("/Users/ammuprakash/Desktop/WEPOF/Screenshots/product_page.png")
            self.driver.find_element_by_xpath(self.place_order_button_by_xpath).click()