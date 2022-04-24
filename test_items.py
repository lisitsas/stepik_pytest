from selenium.common.exceptions import NoSuchElementException


def test_button_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        button = browser.find_element_by_css_selector("button[value='Add to basket']")
        assert button, "Button is invalid"
    except NoSuchElementException:
        return "Button add to basket not found!"
