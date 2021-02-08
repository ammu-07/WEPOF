
class CheckboxGroupProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_by_name = "add-to-cart"


    def checkbox_group_product_page(self, field_value_01, field_value_02):
        try:

            self.driver.find_element_by_name(field_value_01).click()
            self.driver.find_element_by_name(field_value_02).click()
            self.driver.find_element_by_name(self.add_to_cart_button_by_name).click()

        except ValueError:
            print("Field not found")
