from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

email_input_locator = "#id_login-username"
password_input_locator = "#id_login-password"
login_button_locator = "[name='login_submit']"
login_successful_massage_locator = "#messages>div>div"


def test_authorisation_of_existing_user():
    user_email = "m.a.leonov@yandex.ru"
    user_password = "R6vhfB72sV8XN6v"

    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(9)
        browser.get(main_page_link)

        email_input = browser.find_element_by_css_selector(email_input_locator)
        email_input.clear()
        password_input = browser.find_element_by_css_selector(password_input_locator)
        password_input.clear()

        email_input.send_keys(user_email)
        password_input.send_keys(user_password)
        browser.find_element_by_css_selector(login_button_locator).click()

        login_successful_massage = browser.find_element_by_css_selector(login_successful_massage_locator)
        assert "Рады видеть вас снова" in login_successful_massage.text, "Wrong login massage or doesn't exist"

    finally:
        browser.quit()


test_authorisation_of_existing_user()
