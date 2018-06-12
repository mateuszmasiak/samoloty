from __future__ import unicode_literals

from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="/Users/mateuszmasiak/Desktop/chromedriver")

driver.get("http://127.0.0.1:8000/planecrew/")

elem = driver.find_element_by_css_selector("#content > a")
elem.click()
elem = driver.find_element_by_css_selector("#id_username")
elem.send_keys("user1")
elem = driver.find_element_by_css_selector("#id_password")
elem.send_keys("haslouser1")
elem = driver.find_element_by_css_selector("#content > form > button")
elem.click()
elem=driver.find_element_by_css_selector("#content > table > tbody > tr:nth-child(2) > td:nth-child(1) > a")
elem.click()
elem = driver.find_element_by_css_selector("#content > div:nth-child(5) > form > input[type=\"number\"]:nth-child(4)")
elem.send_keys("2")
elem = driver.find_element_by_css_selector("#content > div:nth-child(5) > form > button")
elem.click()
elem = driver.find_element_by_css_selector("#sidebar > a")
elem.click()
elem = driver.find_element_by_css_selector("#sidebar > a:nth-child(2)")
elem.click()
elem = driver.find_element_by_css_selector("body > form > input[type=\"number\"]:nth-child(2)")
elem.send_keys("10")
elem = driver.find_element_by_css_selector("#prz1")
elem.click()
time.sleep(5)
elem = driver.find_element_by_css_selector("body > form > input[type=\"number\"]:nth-child(2)")
elem.send_keys("11")
elem = driver.find_element_by_css_selector("#prz1")
elem.click()
time.sleep(2)
message= driver.find_element_by_css_selector("#myTable > tbody > tr:nth-child(10) > td:nth-child(3)")
assert message.text == "nowe imie"
message= driver.find_element_by_css_selector("#myTable > tbody > tr:nth-child(11) > td:nth-child(3)")
assert message.text == "nowe imie"
