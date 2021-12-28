import time
from selenium import webdriver
class RegisterPage:
    textbox_name_xpath="//input[@name='name']"
    textbox_emailaddress_id="exampleInputEmail1"
    textbox_password_id="exampleInputPassword1"
    textbox_confirmpassword_id="exampleInputPassword2"
    button_Register_xpath="//button[@type='submit']"
    button_signin_xpath="//*[@id='navbarNavDropdown']/ul/li[2]/a"
    linktext_Register_xpath="//a[contains(text(),'Register Now')]"
    #xpath for close alert box for successfull register in register page
    alertbox_success_close_xpath="//*[@id='__next']/div/div[1]/div[1]/button"

    def __init__(self,driver):
        self.driver=driver
    def setName(self,name):
        self.driver.find_element_by_xpath(self.textbox_name_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_name_xpath).send_keys(name)

    def setEmailaddress(self, emailaddress):
        self.driver.find_element_by_id(self.textbox_emailaddress_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.textbox_emailaddress_id).send_keys(emailaddress)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setConfirmpassword(self,confirmpassword):
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).send_keys(confirmpassword)

    def clickRegister(self):
        self.driver.find_element_by_xpath(self.button_Register_xpath).click()

    def clickSignin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clickRegisterNow(self):
        self.driver.find_element_by_xpath(self.linktext_Register_xpath).click()
    def closesuccessalert(self):
        self.driver.find_element_by_xpath(self.alertbox_success_close_xpath).click()
