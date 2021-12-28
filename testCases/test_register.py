import pytest
import time
from selenium import webdriver
from pageObjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
import time
import string
import random
import pytest_html
class Test_001_signin:
    baseURL=ReadConfig.getApplicationURL()

    def test_register(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp=RegisterPage(self.driver)
        self.lp.clickSignin()
        time.sleep(3)
        self.lp.clickRegisterNow()
        time.sleep(3)
        self.lp.setName("testone")
        self.email=random_generator()+"@gmail.com"
        self.lp.setEmailaddress(self.email)
        self.lp.setPassword("876543210")
        self.lp.setConfirmpassword("876543210")
        self.lp.clickRegister()
        time.sleep(3)
        #success_message_id="//*[@id='__next']/div/div[1]/div[2]"
        #act_title=self.driver.title

        self.msg = self.driver.find_element_by_tag_name("body").text
        if "Register Success!" in self.msg:
            self.driver.save_screenshot("/home/ticvictech/PycharmProjects/Sixvercel_project/Screenshots/test_registers.png")
            self.lp.closesuccessalert()
            #self.driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[1]/button").click()
            print("Register user successfull")
            self.driver.close()

        else:
            print("register failure")
            self.driver.close()


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))



