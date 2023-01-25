from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#superclass, parent of all page classes
class BasePage():

    #initializer
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    #finds a specific web element by xpath
    def find_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    #waits 15s until web element is clickeable
    def wait_until_element_is_clickeable(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))
    
    #waits 15s until web element is visible
    def wait_until_element_is_visible(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))

    #once a specified web element is clickeable, performs a click
    def do_click(self, locator):
        self.wait_until_element_is_clickeable(locator)
        self.find_element(locator).click()

    #once a specified web element is visible, performs a send keys
    def do_send_keys(self, locator, value):
        self.wait_until_element_is_visible(locator)
        self.find_element(locator).send_keys(value)

    #get the specified attribute from a web element
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

