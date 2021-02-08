
class CheckboxProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_by_name = "add-to-cart"


    def checkbox_product_page(self, field_name):
        try:

            self.driver.find_element_by_name(field_name).click()
            self.driver.find_element_by_name(self.add_to_cart_button_by_name).click()

        except ValueError:
            print("Field not found")
