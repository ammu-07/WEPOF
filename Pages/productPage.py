from selenium.webdriver.support.ui import Select

class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_by_name = "add-to-cart"

    def product_page(self, field_name, field_value):
        try:

            self.driver.find_element_by_id(field_name).send_keys(field_value)
            self.driver.find_element_by_name(self.add_to_cart_button_by_name).click()
            self.driver.save_screenshot("/Users/ammuprakash/Desktop/WEPOF/Screenshots/product_page.png")
        except ValueError:
            print("Field not found")
            self.driver.save_screenshot("/Users/ammuprakash/Desktop/WEPOF/Screenshots/product_page.png")