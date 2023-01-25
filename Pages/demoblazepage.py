from Pages.basepage import BasePage
from Config.locators import Locators
from selenium.common.exceptions import NoSuchElementException
import time

class DemoBlazePage(BasePage):

    #initializer
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.demoblaze.com/index.html')

    def sign_up_new_user(self, username, password):
        try:
            self.do_click(Locators.sign_up_menu_btn)
            self.do_send_keys(Locators.new_user_name_input, username)
            self.do_send_keys(Locators.new_password_input, password)
            self.do_click(Locators.confirm_sign_up_btn)
            time.sleep(3)
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            raise Exception('Unable to sign up a new user')


    def log_in(self, username, password):
        try:
            self.do_click(Locators.log_in_menu_btn)
            self.do_send_keys(Locators.user_name_input, username)
            self.do_send_keys(Locators.password_input, password)
            self.do_click(Locators.log_in_btn)
        except:
            raise Exception('Unable to log in')

    def check_log_in(self, username):
        try:
            #Waits until welcome message is displayed and validates if the username is present in the welcome message
            self.wait_until_element_is_visible(Locators.welcome_menu)
            welcome_name = self.get_attribute(Locators.welcome_menu, 'textContent')
            return welcome_name == f"Welcome {username}"
        except:
            raise Exception('Unable to check if the user logged in')
        
    def log_out(self):
        try:
            self.do_click(Locators.log_out_btn)
        except:
            raise Exception('Unable to log out')

    def check_log_out(self):
        #Waits until log in button is present in the menu to confirm the user is logged out
        try:
            self.wait_until_element_is_visible(Locators.log_in_menu_btn)
            return True
        except NoSuchElementException:
            return False

    def add_product(self, item):
        try:
            self.do_click(Locators.laptops_category_btn)
            self.do_click(Locators.laptop_item.replace('ReplaceMe', item))
            self.do_click(Locators.add_to_cart_btn)
            time.sleep(2)
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            raise Exception('Unable to add product to the cart')

    def check_cart(self, item):
        try:
            #trys to find the product added to the cart
            self.do_click(Locators.cart_menu_btn)
            self.wait_until_element_is_visible(Locators.item_cart_table_cell.replace('ReplaceMe', item))
            return True
        except:
            return False