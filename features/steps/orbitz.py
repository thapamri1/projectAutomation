from behave import *
from selenium import webdriver
import time
from datetime import date


@given('launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome("C:\Drivers\chromeDriver\chromedriver")
    context.driver = webdriver.Chrome()


@then('Open the website')
def checkOrbitzText(context):
    context.driver.get("https://www.orbitz.com/")


@then('Select Flights')
def selectFlight(context):
    context.driver.find_element_by_link_text("Flights").click()


@then('Select RoundTrip')
def selectRoundTrip(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_link_text("Roundtrip").click()
    # context.driver.find_element_by_id("Leaving from").click()


@then('Click button')
def clickButton(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath("//button[@aria-label='Leaving from']").click()


@then('Enter Leaving From "{leavingCity}" and Going to "{goingCity}" city')
def leavingAndReturningCity(context, leavingCity, goingCity):
    context.driver.find_element_by_xpath("//button[@aria-label='Leaving from']").send_keys(leavingCity)
    context.driver.find_element_by_xpath(
        "//strong[contains(text(),'San Francisco (SFO - San Francisco Intl.)')]").click()
    context.driver.find_element_by_xpath("//button[@aria-label='Going to']").send_keys(goingCity)
    context.driver.find_element_by_xpath("//strong[contains(text(), 'New York (JFK - John F. Kennedy Intl.)')]").click()
    time.sleep(2)


# @then('select select departing date and returning date')
# def selectDates(context):
#     context.driver.find_element_by_xpath("//button[@id='d1-btn']").click()
#     time.sleep(2)
#     # context.browser.find_element_by_css_selector("td.uitk-new-date-picker-day+td").click()
#     today = date.today()
#     print("Today's date:", today)
#     time.sleep(4)


@then('click Search Button')
def clickSearchButton(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()
    time.sleep(5)


@then('select most expensive flight')
def selectMostExpFlight(context):
    context.driver.find_element_by_xpath("//select[@id='sortDropdown']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//option[contains(text(),'Price (Highest)')]").click()
    time.sleep(8)
    # context.driver.find_element_by_xpath("//input[@id='stopFilter_stops-0']").click()
    # time.sleep()


@then('Select Button')
def selectFlight(context):
    context.driver.find_element_by_xpath("//button[@type='button' and contains(., 'Select result 1 when sorted by "
                                         "price')]").click()
    time.sleep(10)


@then('close browser')
def closeBrowser(context):
    context.driver.close()
