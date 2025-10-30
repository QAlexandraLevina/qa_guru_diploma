import allure
from web_baze.pages.authorization_form import AuthorizationForm
from web_baze.pages.header import Header


header = Header()
auth_form = AuthorizationForm()


@allure.title("Проверка элементов хедера и переход по каждой вкладке")
@allure.feature('Test Case #1: Проверка хедера у неавторизованного пользователя')
def test_header_unauthorized_user(setup_browser):
    browser = setup_browser

    browser.open("/")

    with allure.step("Проверка отображения элементов хедера неавторизованным пользователем"):
        header.should_have_menu_items_unauthorized()

    with allure.step("Прокликивание элементов хедера неавторизованным пользователем"):
        header.click_all_tabs_header_unauthorized()


@allure.title("Проверка авторизованного пользователя")
@allure.feature('Test Case #2: Проверка хедера у авторизованного пользователя')
def test_header_authorized_user(authenticated_user):
    # browser = setup_browser

    auth_form.should_authorized_profile()

    with allure.step("Проверка отображения элементов хедера авторизованным пользователем"):
        header.should_have_menu_items_authorized(authenticated_user)

    with allure.step("Прокликивание элементов хедера авторизованным пользователем"):
        header.click_all_tabs_header_authorized(authenticated_user)