import re

class AdminOrdersPage():

    def __init__(self, driver):
        self.driver = driver
        self.view_admin_order_button_by_class_name = "order-view"
        self.field_title_label_by_display_text = "Text 01:"
        self.field_value_label_by_display_text = "field_value"


    def admin_orders_page(self, field_name, field_value):

        self.driver.find_element_by_class_name(self.view_admin_order_button_by_class_name).click()

        try:
            if (field_value in self.driver.page_source):
                return field_value

        except ValueError:
            print("Field not found")
            self.driver.save_screenshot("/Users/ammuprakash/Desktop/WEPOF/Screenshots/product_page.png")
            self.driver.find_element_by_xpath(self.place_order_button_by_name).click()