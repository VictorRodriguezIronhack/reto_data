from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re

options = Options()
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

try:
    button = driver.find_element_by_css_selector("#L2AGLb > div")
except:
    pass

button.click()

box = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")

box.send_keys("e10 precio hoy españa \n")

precio = driver.find_element_by_css_selector("#rso > div.ULSxyf > div > div.kp-blk.c2xzTb > div > div.ifM9O > div > div > div > div > div.wDYxhc > div > div.webanswers-webanswers_table__webanswers-table > table > tbody > tr:nth-child(2) > td:nth-child(2)")

valor = re.findall('\d+.?\d+',precio.text)

valor[0]