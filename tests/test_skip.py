"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have, browser


@pytest.fixture(params=[(1011, 600), (1440, 800), (390, 844)])
def browser_size(request):
    if request.param[0] < 1012:  # mobile
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return 'mobile'
    if request.param[0] >= 1012:  # desktop
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return 'desktop'


def test_github_desktop(browser_size):
    if browser_size == 'mobile':
        pytest.skip(reason='Запускаем только мобильные тесты')
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_size):
    if browser_size == 'desktop':
        pytest.skip(reason='Запускаем только desktop-тесты')
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
