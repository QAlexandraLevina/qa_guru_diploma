import allure
import pytest
from web_baze.pages.authorization_form import AuthorizationForm


authorization_form = AuthorizationForm()

@pytest.mark.web
@allure.title("Авторизация и проверка авторизации пользователя")
def test_authorization_form(setup_browser, open_base_page, user_authorized):
    # browser = setup_browser


    with allure.step("Авторизация пользователя"):
        authorization_form.authorization_user(user_authorized)

    with allure.step("Проверка авторизованного пользователя"):
        authorization_form.should_authorized_profile()