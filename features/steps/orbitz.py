from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome("C:\Drivers\chromeDriver\chromedriver")
    context.driver = webdriver.Chrome()


@then('Open the website')
def checkOrbitzText(context):
    context.driver.get("https://www.orbitz.com/")


@then('close browser')
def closeBrowser(context):
    context.driver.close()
