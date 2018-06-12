 -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


driver = webdriver.Chrome(executable_path="/Users/mateuszmasiak/Desktop/chromedriver")
driver = webd
adfs
river.Chrome()
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
elem.send_keys("2915")
elem = driver.find_element_by_css_selector("#prz1")
elem.send_keys("2965")
elem = driver.find_element_by_css_selector("#prz1")
driver.refresh()
time.sleep(2)
elem.click()
time.sleep(2)
