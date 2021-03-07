link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_rus_text_of_button(browser):
    browser.get(link)
    add_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_button.text in "Добавить в корзину Añadir al carrito Ajouter au panier Add to basket" , \
        "Wrong text of add-button, or not on 'ru', 'en-GB', 'es', 'fr' language!"