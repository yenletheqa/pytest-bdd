from pytest_bdd import scenario, given, when, then, parsers

from pages.home_page import HomePage


@scenario('webdriver.feature', 'start browsing')
def test_webdriver():
    pass


@given("we have a opened Chrome browser")
def open_chrome(driver):
    driver.maximize_window()


@when(parsers.cfparse("we navigate to {website}"))
def navigate(driver, website):
    driver.get(website)


@then(parsers.cfparse("we should see {content}"))
def content(driver):
    home_page = HomePage(driver)
    assert home_page.is_logo_displayed()
