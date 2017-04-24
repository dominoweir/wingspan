#ScriptName : testForm.py
#---------------------
from selenium import webdriver
import os

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "../compute.html"

flightNumber = "7"
startLocation = "University of Texas at Austin, Austin, TX"
timingPref = "early"
withKids = "no"

xpaths = { 'flightNumber' : "//input[@name='q1']",
           'startLocation' : "//input[@name='q2']",
           'timingPref' :   "//input[@name='q3']",
           'withKids' : "//input[@name='q4']"
         }

os.environ['PATH'] = "/Users/dominoweir/Documents/wingspan/test"
print os.environ['PATH']
driver = webdriver.Chrome()
driver.get(baseurl)
driver.maximize_window()
results = open("formExpected.txt",'w')

# write sample data in to text boxes
driver.find_element_by_xpath(xpaths['flightNumber']).send_keys(flightNumber)
driver.find_element_by_xpath(xpaths['startLocation']).send_keys(startLocation)
driver.find_element_by_xpath(xpaths['timingPref']).send_keys(timingPref)
driver.find_element_by_xpath(xpaths['withKids']).send_keys(withKids)

# click submit button
try:
    driver.find_element_by_xpath(xpaths['submitButton']).click()
    results.write("Simple test was a success.")
except ElementNotVisibleException, e:
    results.write("Simple test failed.")
    results.write("Error encountered: " + e)

results.close()
driver.quit()
