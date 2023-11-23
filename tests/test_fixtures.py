"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import by, have
from selene.support.shared import browser


@pytest.fixture
def desktop():
    browser.config.window_width = 1440
    browser.config.window_height = 800

    yield
    browser.quit()


@pytest.fixture
def mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844

    yield
    browser.quit()


def test_github_desktop(desktop):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile):
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
