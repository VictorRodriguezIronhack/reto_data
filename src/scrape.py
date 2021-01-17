import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import tqdm
import json
import pandas as pd

class Scrape():
    '''
    Collection of functions used for scraping the website 
    '''

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
         self.driver.find_element_by_xpath('//*[@id="privacy_block"]/div[4]/p/button[1]').click()


    def select_city(self, city = 242):

        city = str(city)
        select = Select(self.driver.find_element_by_id('localidad'))
        select.select_by_value(city)


    def input_form(self):
        self.driver.find_element_by_xpath('//*[@id="Busqueda"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[5]/input').click()



    def extract_stations_url(self):
 
        tmp_list = []
    
        page = self.driver.page_source
        soup = BeautifulSoup(page, features="lxml")

        stations_html = soup.find('tbody').find_all('a')


        for station in stations_html:
            url_path = station['href']
            tmp_list.append(url_path)

        
        return tmp_list

    def click_siguiente(self):
        self.driver.find_element_by_xpath('//*[@id="rdos_gasolineras_next"]').click()



    def check_end(self, example, stations_list):

        if example in stations_list:
            return True
        
        return False


    def scrape_urls(self):
        stations_list = []

        check_end = False

        while not check_end:
            candidates = self.extract_stations_url()

            

            check_end = self.check_end(candidates[0], stations_list)

            if not check_end:
                stations_list.extend(candidates)

            self.click_siguiente()
            time.sleep(0.5)

        return stations_list


    def scrape_station(self):
        page = self.driver.page_source
        soup = BeautifulSoup(page, features="lxml")
        stations_html = soup.select('div.contenido_cubo')[0].find_all('tbody')

        name_data = soup.select('div.cubo')[0].find_all('h1')[0]
        name =name_data.text
        direction = name_data.find('span').text

        tmp_list =[]

        for item in stations_html:
            try:
                gas_type = item.find('th').text
                price = item.find_all('td')[0].text
            except:
                continue
            else:
                tmp_list.append({'name': name, 'direction': direction, 'gas_type': gas_type, 'price': price })



        return tmp_list


    def scrape_all(self, stations_list):

        full_data = []

        for station in stations_list:

            self.driver.get(station)
            time.sleep(0.5)
            data = self.scrape_station()
            full_data.extend(data)

            time.sleep(1)


        return full_data



















