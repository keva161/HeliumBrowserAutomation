from helium import *

def docket_page_firefox():
    start_chrome('https://docket-test.herokuapp.com/')
    menu_text = Text(to_right_of='Login').value
    kill_browser()
    return menu_text

def test_docket_should_have_register_text_firefox():
    result = docket_page_firefox()
    assert 'Register' in result