"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import have, browser


@pytest.fixture(params=['desktop', 'mobile'])
def browser_size(request):
    if request.param == 'desktop':
        browser.config.window_width = 1440
        browser.config.window_height = 800

    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844

    yield
    browser.quit()


@pytest.mark.parametrize("browser_size", ['desktop'], indirect=True)
def test_github_desktop(browser_size):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", ['mobile'], indirect=True)
def test_github_mobile(browser_size ):
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
