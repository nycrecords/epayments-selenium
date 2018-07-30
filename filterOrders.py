from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest
import time

class filterResults(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def change_type(self, category):
        # self.change_category('//*[@id="grid-column-search"]/div[2]/form/div[3]/div/div[2]/div[1]')
        # the above code is the format for selecting the tab options for type
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[3]/div/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(category).click()
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/button[2]').click()
        time.sleep(1.5)

    def change_status(self, status):
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[4]/div/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(status).click()
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/button[2]').click()
        time.sleep(1.5)

    def filter_by_type(self, user_type):
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[6]/div/div/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[6]/div/div/div/div/input').send_keys('07/16/2018')
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[6]/div/div/div/div/input').send_keys(Keys.ENTER)

        for num in range(1,16):
            self.change_type('//*[@id="grid-column-search"]/div[2]/form/div[3]/div/div[2]/div[' + str(num) + ']')

    def filter_by_status(self, user_type):
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[6]/div/div/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[6]/div/div/div/div/input').send_keys('07/16/2018')
        self.driver.find_element_by_xpath('//*[@id="grid-column-search"]/div[2]/form/div[6]/div/div/div/div/input').send_keys(Keys.ENTER)

        for num in range (1,12):
            self.change_status('//*[@id="grid-column-search"]/div[2]/form/div[4]/div/div[2]/div[' + str(num) + ']')