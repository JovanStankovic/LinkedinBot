import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedinBot:

    def __init__(self,username,password):
        self.driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"session_key\"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\"session_password\"]')\
            .send_keys(password)
        time.sleep(3)

    def get_followers(self):
        self.driver.find_element_by_xpath('//a[contains(@href,"/mynetwork/")]')\
            .click()
        i = 0
        time.sleep(6)
        while i < 24:
            self.driver.find_element_by_xpath('//button[@data-control-name="people_connect"]')\
                .click()
            time.sleep(2)
            i+=1

f = open("secret.txt", "r")
username = f.readline()
password = f.readline()

lb = LinkedinBot(username,password)
lb.get_followers()
