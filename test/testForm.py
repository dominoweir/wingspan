# ScriptName : testForm.py
# ---------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


def run():
    baseurl = "https://wingspan-app.herokuapp.com/compute.html"

    flightNumber = "7"
    startLocation = "University of Texas at Austin, Austin, TX"
    timingPref = "early"
    withKids = "no"

    xpaths = {'flightNumber': "//input[@name='q1']",
              'startLocation': "//input[@name='q2']",
              'timingPref': "//input[@name='q3']",
              'withKids': "//input[@name='q4']",
              'next': "//button[@name='next']",
              'submitButton': "//button[@name='submitButton']"
              }

    os.environ['PATH'] = "/Users/nickwhite/Documents/Chrome"
    driver = webdriver.Chrome()
    driver.get(baseurl)
    driver.maximize_window()
    results = open("formActual.txt", 'w')

    # write sample data in to text boxes
    driver.find_element_by_xpath(xpaths['flightNumber']).send_keys(flightNumber)
    driver.find_element_by_xpath(xpaths['next']).click()
    driver.find_element_by_xpath(xpaths['startLocation']).send_keys(startLocation)
    driver.find_element_by_xpath(xpaths['next']).click()
    driver.find_element_by_xpath(xpaths['timingPref']).send_keys(timingPref)
    driver.find_element_by_xpath(xpaths['next']).click()
    driver.find_element_by_xpath(xpaths['withKids']).send_keys(withKids)

    # click submit button
    try:
        driver.find_element_by_xpath(xpaths['next']).click()
        results.write("Simple test was a success.\n")
    except Exception, e:
        results.write("Simple test failed.\n")
        results.write(str(e))

    results.close()
    driver.quit()
