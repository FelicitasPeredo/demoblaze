from Pages.demoblazepage import DemoBlazePage
from Utilities.handlers import DatasetHandlers
import time, json, pytest

#deserialize supporting file-like object containing a JSON document to a Python object
#change path if needed
with open("C:\\Users\\Felicitas Peredo\\Documents\\demoblaze\\Config\\dataset.json") as jsonFile:
    file = json.load(jsonFile)

class TestCases():
    #parametrize the test with possible inputs, in this case only three
    @pytest.mark.parametrize("username, password, item", DatasetHandlers.test_handler(file))
    #Dar de alta un usuario
    def test_sign_up(self, init_driver, username, password, item):
        driver = init_driver
        self.demoplazepage = DemoBlazePage(driver)
        self.demoplazepage.sign_up_new_user(username, password)

    #Login y logout con el usuario dado de alta
    @pytest.mark.parametrize("username, password, item", DatasetHandlers.test_handler(file))
    def test_log_in_log_out(self, init_driver, username, password, item):
        driver = init_driver
        self.demoplazepage = DemoBlazePage(driver)
        self.demoplazepage.log_in(username, password)
        logged_in = self.demoplazepage.check_log_in(username)
        #only if the user logged in continues to log out and check if it logged out
        if logged_in:
            self.demoplazepage.log_out()
            logged_out =  self.demoplazepage.check_log_out()
            assert logged_out
        else:
            raise Exception('Unable to Log in')

    #Agregar una laptop al carrito y comprobar que se agrego al carrito
    @pytest.mark.parametrize("username, password, item", DatasetHandlers.test_handler(file))
    def test_add_laptop_to_cart(self, init_driver, username, password, item):
        driver = init_driver
        self.demoplazepage = DemoBlazePage(driver)
        self.demoplazepage.log_in(username, password)
        logged_in = self.demoplazepage.check_log_in(username)
        #only if the user logged in continues to add the product and check if it's in the cart
        if logged_in:
            self.demoplazepage.add_product(item)
            item_added = self.demoplazepage.check_cart(item)
            assert item_added
        else:
            raise Exception('Unable to Log in')
        
