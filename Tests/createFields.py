from selenium import webdriver
import unittest
import xlrd
import xlwt
from xlutils.copy import copy

from Pages.loginWordPress import LoginWordPress
from Pages.addFields import AddField
from Pages.productPage import ProductPage
from Pages.cartPage import CartPage
from Pages.checkoutPage import CheckoutPage
from Pages.UserOrdersPage import OrdersPage
from Pages.adminOrdersPage import AdminOrdersPage
from Pages.addSelectFields import AddSelectField
from Pages.selectProductPage import SelectProductPage
from Pages.addCheckboxField import AddCheckboxField
from Pages.checkboxProductPage import CheckboxProductPage
from Pages.addCheckboxGroupField import AddCheckboxGroupField
from Pages.checkboxGroupProductPage import CheckboxGroupProductPage

class AddField_WEPO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/ammuprakash/Desktop/Python/chromedriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("http://test1.floopbox.com/wp-admin/edit.php?post_type=product&page=thwepof_extra_product_options")
        login = LoginWordPress(cls.driver)
        login.login_wordpress_dashboard("Ammu", "qa@india#")


    # def test_01_create_field(self):
    #     driver = self.driver
    #
    #     self.workbook = xlrd.open_workbook('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #     self.workbook1 = copy(self.workbook)
    #     self.sheet = self.workbook.sheet_by_index(0)
    #     self.sheet1 = self.workbook1.get_sheet(0)
    #
    #     for i in range(self.sheet.nrows):
    #         self.value_field_type = self.sheet.cell_value(i, 0)
    #         self.value_field_name = self.sheet.cell_value(i, 1)
    #         self.value_field_title = self.sheet.cell_value(i, 2)
    #         self.value_field_value = self.sheet.cell_value(i, 3)
    #         self.value_field_name_str = str(self.value_field_name)
    #         self.value_field_title_str = str(self.value_field_title)
    #         self.value_field_type_str = str(self.value_field_type)
    #         self.value_field_value_str = str(self.value_field_value)
    #         self.driver.get("http://test1.floopbox.com/wp-admin/edit.php?post_type=product&page=thwepof_extra_product_options")
    #
    #         #Creating a Field from WEPOF Settings #
    #         add_field = AddField(driver)
    #         add_field.create_field(self.value_field_type_str, self.value_field_name_str, self.value_field_title_str)
    #         print(self.value_field_type, "Field created successfully")
    #         self.sheet1.write(i, 4, 'Field created successfully')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #         self.driver.get("http://test1.floopbox.com/index.php/product/test1/")
    #
    #         #Previewing the created field at Product page#
    #         product_page = ProductPage(driver)
    #         product_page.product_page(self.value_field_name, self.value_field_value_str)
    #         self.sheet1.write(i, 5, 'Field displayed successfully @Product page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at Cart page#
    #         self.driver.get("https://test1.floopbox.com/index.php/cart/")
    #         cart_page = CartPage(driver)
    #         cart_page.cart_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 6, 'Field displayed successfully @Cart page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at Checkout page#
    #         self.driver.get("https://test1.floopbox.com/index.php/checkout/")
    #         checkout_page = CheckoutPage(driver)
    #         checkout_page.checkout_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 7, 'Field displayed successfully @Checkout page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at My Account >> View Order page#
    #         self.driver.get("https://test1.floopbox.com/index.php/my-account/orders/")
    #         orders_page = OrdersPage(driver)
    #         orders_page.orders_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 8, 'Field displayed successfully @My Account >> View Order page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at WooCommerce >> Orders#
    #         self.driver.get("https://test1.floopbox.com/wp-admin/edit.php?post_type=shop_order")
    #         admin_orders_page = AdminOrdersPage(driver)
    #         admin_orders_page.admin_orders_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 9, 'Field displayed successfully @WooCommerce >> Orders >> View Order page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    # def test_02_create_select_field(self):
    #     driver = self.driver
    #     self.workbook = xlrd.open_workbook('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #     self.workbook1 = copy(self.workbook)
    #     self.sheet = self.workbook.sheet_by_index(1)
    #     self.sheet1 = self.workbook1.get_sheet(1)
    #
    #     for i in range(self.sheet.nrows):
    #         self.value_field_type = self.sheet.cell_value(i, 0)
    #         self.value_field_name = self.sheet.cell_value(i, 1)
    #         self.value_field_title = self.sheet.cell_value(i, 2)
    #         self.value_field_options = self.sheet.cell_value(i, 3)
    #         self.value_field_value = self.sheet.cell_value(i, 4)
    #
    #         self.value_field_name_str = str(self.value_field_name)
    #         self.value_field_title_str = str(self.value_field_title)
    #         self.value_field_type_str = str(self.value_field_type)
    #         self.value_field_options_str = str(self.value_field_options)
    #         self.value_field_value_str = str(self.value_field_value)
    #
    #         self.driver.get("http://test1.floopbox.com/wp-admin/edit.php?post_type=product&page=thwepof_extra_product_options")
    #
    #         # Creating a Field from WEPOF Settings #
    #         create_select_field = AddSelectField(driver)
    #         create_select_field.create_select_field(self.value_field_type_str, self.value_field_name_str, self.value_field_title_str, self.value_field_options_str)
    #         print(self.value_field_type, "Field created successfully")
    #         self.sheet1.write(i, 5, 'Field created successfully')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #         self.driver.get("http://test1.floopbox.com/index.php/product/test1/")
    #
    #         #Previewing the created field at Product page#
    #         select_product_page = SelectProductPage(driver)
    #         select_product_page.select_product_page(self.value_field_name, self.value_field_value_str)
    #         self.sheet1.write(i, 6, 'Field displayed successfully @Product page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at Cart page#
    #         self.driver.get("https://test1.floopbox.com/index.php/cart/")
    #         cart_page = CartPage(driver)
    #         cart_page.cart_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 7, 'Field displayed successfully @Cart page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at Checkout page#
    #         self.driver.get("https://test1.floopbox.com/index.php/checkout/")
    #         checkout_page = CheckoutPage(driver)
    #         checkout_page.checkout_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 8, 'Field displayed successfully @Checkout page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at My Account >> View Order page#
    #         self.driver.get("https://test1.floopbox.com/index.php/my-account/orders/")
    #         orders_page = OrdersPage(driver)
    #         orders_page.orders_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 9, 'Field displayed successfully @My Account >> View Order page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at WooCommerce >> Orders#
    #         self.driver.get("https://test1.floopbox.com/wp-admin/edit.php?post_type=shop_order")
    #         admin_orders_page = AdminOrdersPage(driver)
    #         admin_orders_page.admin_orders_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 10, 'Field displayed successfully @WooCommerce >> Orders >> View Order page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')

    # def test_03_create_checkbox_field(self):
    #     driver = self.driver
    #     self.workbook = xlrd.open_workbook('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #     self.workbook1 = copy(self.workbook)
    #     self.sheet = self.workbook.sheet_by_index(2)
    #     self.sheet1 = self.workbook1.get_sheet(2)
    #
    #     for i in range(self.sheet.nrows):
    #         self.value_field_type = self.sheet.cell_value(i, 0)
    #         self.value_field_name = self.sheet.cell_value(i, 1)
    #         self.value_field_title = self.sheet.cell_value(i, 2)
    #         self.value_field_value = self.sheet.cell_value(i, 3)
    #
    #         self.value_field_name_str = str(self.value_field_name)
    #         self.value_field_title_str = str(self.value_field_title)
    #         self.value_field_type_str = str(self.value_field_type)
    #         self.value_field_value_str = str(self.value_field_value)
    #
    #         # Creating a Field from WEPOF Settings #
    #         create_checkbox_field = AddCheckboxField(driver)
    #         create_checkbox_field.create_checkbox_field(self.value_field_type_str, self.value_field_name_str, self.value_field_title_str, self.value_field_value)
    #         print(self.value_field_type, "Field created successfully")
    #         self.sheet1.write(i, 4, 'Field created successfully')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #         self.driver.get("http://test1.floopbox.com/index.php/product/test1/")
    #
    #         # Previewing the created field at Product page#
    #         checkbox_product_page = CheckboxProductPage(driver)
    #         checkbox_product_page.checkbox_product_page(self.value_field_name)
    #         self.sheet1.write(i, 5, 'Field displayed successfully @Product page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at Cart page#
    #         self.driver.get("https://test1.floopbox.com/index.php/cart/")
    #         cart_page = CartPage(driver)
    #         cart_page.cart_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 6, 'Field displayed successfully @Cart page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at Checkout page#
    #         self.driver.get("https://test1.floopbox.com/index.php/checkout/")
    #         checkout_page = CheckoutPage(driver)
    #         checkout_page.checkout_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 7, 'Field displayed successfully @Checkout page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at My Account >> View Order page#
    #         self.driver.get("https://test1.floopbox.com/index.php/my-account/orders/")
    #         orders_page = OrdersPage(driver)
    #         orders_page.orders_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 8, 'Field displayed successfully @My Account >> View Order page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    #         # Previewing the created field at WooCommerce >> Orders#
    #         self.driver.get("https://test1.floopbox.com/wp-admin/edit.php?post_type=shop_order")
    #         admin_orders_page = AdminOrdersPage(driver)
    #         admin_orders_page.admin_orders_page(self.value_field_type_str, self.value_field_value_str)
    #         self.sheet1.write(i, 9, 'Field displayed successfully @WooCommerce >> Orders >> View Order page')
    #         self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
    #
    def test_04_create_checkbox_field(self):
        driver = self.driver
        self.workbook = xlrd.open_workbook('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
        self.workbook1 = copy(self.workbook)
        self.sheet = self.workbook.sheet_by_index(3)
        self.sheet1 = self.workbook1.get_sheet(3)

        for i in range(self.sheet.nrows):
            self.value_field_type = self.sheet.cell_value(i, 0)
            self.value_field_name = self.sheet.cell_value(i, 1)
            self.value_field_title = self.sheet.cell_value(i, 2)
            self.field_value = self.sheet.cell_value(i, 3)
            self.field_value_01 = self.sheet.cell_value(i, 4)
            self.field_value_02 = self.sheet.cell_value(i, 5)

            self.value_field_name_str = str(self.value_field_name)
            self.value_field_title_str = str(self.value_field_title)
            self.value_field_type_str = str(self.value_field_type)
            self.value_field_value_str = str(self.value_field_value)
            self.field_value_01_str = str(field_value_01)
            self.field_value_02_str = str(field_value_02)

            # Creating a Field from WEPOF Settings #
            create_checkbox_group_field = AddCheckboxGroupField(driver)
            create_checkbox_group_field.create_checkbox_group_field(self.value_field_type_str, self.value_field_name_str, self.value_field_title_str, self.value_field_value)
            print(self.value_field_type, "Field created successfully")
            self.sheet1.write(i, 4, 'Field created successfully')
            self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')
            self.driver.get("http://test1.floopbox.com/index.php/product/test1/")

            # Previewing the created field at Product page#
            checkbox_group_product_page = CheckboxGroupProductPage(driver)
            checkbox_group_product_page.checkbox_group_product_page(self.field_value_01_str, self.field_value_02_str)
            self.sheet1.write(i, 5, 'Field displayed successfully @Product page')
            self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')

            # Previewing the created field at Cart page#
            self.driver.get("https://test1.floopbox.com/index.php/cart/")
            cart_page = CartPage(driver)
            cart_page.cart_page(self.value_field_type_str, self.value_field_value_str)
            self.sheet1.write(i, 6, 'Field displayed successfully @Cart page')
            self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')

            # Previewing the created field at Checkout page#
            self.driver.get("https://test1.floopbox.com/index.php/checkout/")
            checkout_page = CheckoutPage(driver)
            checkout_page.checkout_page(self.value_field_type_str, self.value_field_value_str)
            self.sheet1.write(i, 7, 'Field displayed successfully @Checkout page')
            self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')

            # Previewing the created field at My Account >> View Order page#
            self.driver.get("https://test1.floopbox.com/index.php/my-account/orders/")
            orders_page = OrdersPage(driver)
            orders_page.orders_page(self.value_field_type_str, self.value_field_value_str)
            self.sheet1.write(i, 8, 'Field displayed successfully @My Account >> View Order page')
            self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')

            # Previewing the created field at WooCommerce >> Orders#
            self.driver.get("https://test1.floopbox.com/wp-admin/edit.php?post_type=shop_order")
            admin_orders_page = AdminOrdersPage(driver)
            admin_orders_page.admin_orders_page(self.value_field_type_str, self.value_field_value_str)
            self.sheet1.write(i, 9, 'Field displayed successfully @WooCommerce >> Orders >> View Order page')
            self.workbook1.save('/Users/ammuprakash/Downloads/WEPO Fields.xlsx')

    @classmethod
    def tearDownClass(cls):
        print("Test completed successfully")
        cls.driver.close()
        cls.driver.quit()