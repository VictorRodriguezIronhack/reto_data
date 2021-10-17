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

box.send_keys("Precio Gasolina 98 hoy \n")

precio = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/table/tbody/tr[2]/td[1]")

valor = re.findall('\d+.?\d+',precio.text)

valor[0]