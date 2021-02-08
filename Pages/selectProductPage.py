from selenium.webdriver.support.ui import Select

class SelectProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_by_name = "add-to-cart"


    def select_product_page(self, field_name, field_value):
        try:

            self.select_field = Select(self.driver.find_element_by_name(field_name))
            self.select_field.select_by_value(field_value)
            self.driver.find_element_by_name(self.add_to_cart_button_by_name).click()

        except ValueError:
            print("Field not found")
