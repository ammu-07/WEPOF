import re

class CartPage():

    def __init__(self, driver):
        self.driver = driver
        self.proceed_to_checkout_button_by_name = "//*[@id=\"post-7\"]/div[1]/div/div[2]/div/div/a"
        self.field_title_label_by_display_text = "Text 01:"


    def cart_page(self, field_name, field_value):

        try:
            if (field_value in self.driver.page_source):
                return field_value


        except ValueError:
            print("Field not found")
            self.driver.save_screenshot("/Users/ammuprakash/Desktop/WEPOF/Screenshots/product_page.png")
            self.driver.find_element_by_xpath(self.proceed_to_checkout_button_by_name).click()