"""
system test for Sixvercel_project
-------------------------------------------
platform     linux
Python       3.8.10
pytest       6.2.4
pytest-sugar 0.9.4
project-name Sixvercel
"""
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from pageObjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
from utilities.customLoger import LogGen
import time,string,random,pytest
#Create a class for a test_system.py file
class Test_003_systemtest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_system(self,setup):
        self.logger.info("*****Test_003_systemtest*****")
        self.logger.info("*****Negative login test without register user*****")
        #setup function for driver located in conftest.py file
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.clickSignin()
        self.email = random_generator() + "@gmail.com"
        self.lp.setUsername(self.email)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(3)
        self.msg = self.driver.find_element_by_tag_name("body").text

        if "This user does not exist." in self.msg:
            self.driver.save_screenshot("Screenshots/success_reports/successlogin.png")
            self.lp.clickalertclose()
            self.logger.info("*****negative login test success*****")
            #Go for register page and register user secion
            self.lps = RegisterPage(self.driver)
            self.lps.clickRegisterNow()
            self.logger.info("*****Verifying new register*****")
            time.sleep(3)
            self.lps.setName("testone")
            self.lps.setEmailaddress(self.email)
            self.lps.setPassword("876543210")
            self.lps.setConfirmpassword("876543210")
            self.lps.clickRegister()
            time.sleep(3)
            #close success alert box
            self.lps.closesuccessalert()
            time.sleep(2)
            self.logger.info("****Success new register user!*****")

            #click login
            self.logger.info("*****Login after regitred user*****")
            self.driver.find_element_by_xpath("//*[@id='__next']/div/div[2]/form/p/a").click()
            self.lp.setUsername(self.email)
            self.lp.setPassword("876543210")
            self.lp.clicklogin()
            time.sleep(3)
            if "Login Success!" in self.msg:
                self.logger.info("***Login success with register user!******")
                self.lp.clickalertclose()
                time.sleep(2)
                self.lp.clicklogout()

                self.driver.close()
            else:
                self.logger.info("*****Test_003_systemtest completed*****")
                self.driver.close()
        else:
            print("Login error")
            self.driver.save_screenshot("Screenshots/Failure_reports/failure_negativelogin.png")
            self.logger.info("*****Negative login test failed!*****")
            self.driver.close()

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))




