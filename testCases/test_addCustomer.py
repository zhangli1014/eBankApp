import string
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ebankCustomerPage import AddCustomer
from pageObjects.ebankLoginPage import LoginPage
from utilities.readConfig import ReadConfig
from utilities.customerLogger import LogGen
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_003_AddCustomer:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddCustomer(self,setup):
        self.logger.info('*************Test_003_AddCustomer************')

        self.driver =setup
        #open the login page
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('****************Login successful*****************')

        self.logger.info('***********Starting add new customer**********')
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickNewCustome()
        self.logger.info('***********Providing  new customer info**********')
        self.email = random_generator()+"@gmail.com"
        self.addcust.setCustomerName('zhanglig')
        self.addcust.setGender('female')
        self.addcust.setBirth('0019810924')
        self.addcust.setAddress('China')
        self.addcust.setCity('Nanjing')
        self.addcust.setState('ON')
        self.addcust.setPin('123456')
        self.addcust.setMobile('862487735286')
        self.addcust.setEmail(self.email)
        self.addcust.setPass('123456')
        time.sleep(5)

        self.addcust.clickSubmit()
        self.logger.info('***********Save  customer info**********')

        self.msg = self.driver.find_element(By.XPATH,"//p[@class='heading3']").text

        if self.msg == 'Customer Registered Successfully!!!':
            self.logger.info('***********Add new customer passed**********')
            self.uerid =self.driver.find_element(By.XPATH,"//td[text()=\"Customer ID\"]/following-sibling::*[1]")
            print(self.uerid)
            assert True
        else:
            WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            text = self.driver.switch_to.alert.text
            self.logger.info('***********Add new customer failed,%s**********',text)
            assert False

def random_generator(size =8,chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
