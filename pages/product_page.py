from selenium.webdriver.common.by import By 
from .base_page import BasePage 
 
class ProductPage(BasePage): 
    def __init__(self, browser): 
        super().__init__(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/") 
 
    # Локаторы элементов 
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket") 
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success") 
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") 
    REVIEWS_TAB = (By.CSS_SELECTOR, "#reviews") 
 
    # Методы-действия 
    def add_to_cart(self): 
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click() 
 
    def go_to_reviews(self): 
        self.browser.find_element(*self.REVIEWS_TAB).click() 
 
    # Методы-проверки 
    def should_have_add_button(self): 
        assert self.is_element_present(*self.ADD_TO_CART_BUTTON), "Add to cart button not found" 
 
    def should_have_success_message(self): 
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Success message not found" 
 
    def should_have_product_name(self): 
        assert self.is_element_present(*self.PRODUCT_NAME), "Product name not found" 
