from selenium.webdriver.common.by import By 
from .base_page import BasePage 
 
class LoginPage(BasePage): 
    def __init__(self, browser): 
        super().__init__(browser, "http://selenium1py.pythonanywhere.com/accounts/login/") 
 
    def should_be_login_form(self): 
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented" 
 
    def should_be_register_form(self): 
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is not presented" 
