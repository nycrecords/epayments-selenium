from selenium import webdriver
import unittest
import time

# logs into the website

class Login(unittest.TestCase):

    admin_username = 'bwaite@records.nyc.gov'
    admin_password = '1234'
    
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login(self, user_type):
        if user_type == 'admin':
            self.driver.find_element_by_xpath('//*[@id="center"]/button').click()
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[1]/div/input').send_keys(self.admin_username)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[2]/div/input').send_keys(self.admin_password)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/button[1]').click()
        time.sleep(1)