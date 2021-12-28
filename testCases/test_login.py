import pytest ,time ,string ,random ,pytest_html
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
class Test_002_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_negativelogin(self,setup):
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.clickSignin()
        self.email=random_generator()+"@gmail.com"
        self.lp.setUsername(self.email)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(3)
        self.msg = self.driver.find_element_by_tag_name("body").text
        if "Login Success!" in self.msg:
            self.driver.save_screenshot("Screenshots/success_reports/successlogin.png")
            print("Negative login test")
            print("Login success")
            self.driver.close()
        else:
            self.driver.save_screenshot("Screenshots/Failure_reports/failurelogin.png")
            self.driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[1]/button").click()
            print("Negative login test")
            print("login unsuccess")
            self.driver.close()

    def test_possitivelogin(self,setup):
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.clickSignin()
        self.lp.setUsername(self.email)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(3)
        self.msg = self.driver.find_element_by_tag_name("body").text
        if "Login Success!" in self.msg:
            self.driver.save_screenshot("Screenshots/success_reports/successlogin.png")
            print("Possitive login test")
            print("Login success")
            self.driver.close()
        else:
            self.driver.save_screenshot("Screenshots/Failure_reports/failurelogin.png")
            self.driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[1]/button").click()
            print("Possitive login test")
            print("login unsuccess")
            self.driver.close()

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))




