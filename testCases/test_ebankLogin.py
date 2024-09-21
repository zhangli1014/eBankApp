import time
import pytest
from selenium import webdriver
#import sys
#sys.path.append('D:\\autotest\\SeleniumWebDriverProject\\nopCommercialApp\\')
from pageObjects.ebankLoginPage import LoginPage
from utilities.readConfig import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    base_url= ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePage_Title(self,setup):
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying home page title********')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        act_tile = self.driver.title

        if act_tile=='Guru99 Bank Home Page':
            self.logger.info('***********Home page test is passed********')
            assert True
        else:
            self.logger.error('***********Home page test is failed********')
            self.driver.save_screenshot('.\\Screenshot\\'+'test_homePage_Title.png')
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginpage(self,setup):
        self.logger.info('***********Verifying Login page title********')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_tile = self.driver.title
        print(act_tile)
        if act_tile=='Guru99 Bank Manager HomePage':
            self.logger.info('***********Login page test is passed********')
            assert True
        else:
            self.logger.error('***********Login page test is failed********')
            self.driver.save_screenshot('.\\Screenshot\\' + 'test_loginpage.png')
            assert False
        self.driver.close()

if __name__=='__main__':
    pytest.main(['-v','test_eBankLogin.py'])
