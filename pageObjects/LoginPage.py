import string
import time
from random import random

from selenium import webdriver
class Loginpage:
    textbox_username_id = "exampleInputEmail1"
    textbox_password_id = "exampleInputPassword1"
    login_button_xpath = "//button[@type='submit']"
    link_logout_linktext_xpath="//*[@id='navbarNavDropdown']/ul/li[2]/div/button"
    button_signin_xpath = "//*[@id='navbarNavDropdown']/ul/li[2]/a"
    alertbox_usernotexit_close_xpath="//*[@id='__next']/div/div[1]/div[1]/button"
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        time.sleep(4)
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext_xpath).click()
    def clickSignin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()
    def clickalertclose(self):
        self.driver.find_element_by_xpath(self.alertbox_usernotexit_close_xpath).click()
