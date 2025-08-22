from pages.product_page import ProductPage 
 
def test_guest_can_add_product_to_cart(browser): 
    page = ProductPage(browser) 
    page.open() 
    page.should_have_add_button() 
    page.add_to_cart() 
    page.should_have_success_message() 
 
def test_guest_can_see_product_details(browser): 
    page = ProductPage(browser) 
    page.open() 
    page.should_have_product_name() 
