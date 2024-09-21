import time
import pytest
from selenium import webdriver
from pageObjects.ebankLoginPage import LoginPage
from utilities.readConfig import ReadConfig
from utilities.customerLogger import LogGen
from utilities import ExcelUtilities


class Test_002_DDT_Login:
    base_url= ReadConfig.getApplicationURL()
    path = './/TestData//LoginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info('***********Test_002_DDT_Login********')
        self.logger.info('***********Verifying Login DDT title********')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.lp =LoginPage(self.driver)
        self.rows = ExcelUtilities.getRowCount(self.path,'Sheet1')
        self.columns = ExcelUtilities.getColumnCount(self.path, 'Sheet1')
        for i in range(2,self.rows+1):
            self.username = ExcelUtilities.readData(self.path,'Sheet1',i,1)
            self.password = ExcelUtilities.readData(self.path, 'Sheet1', i, 2)
            self.exp = ExcelUtilities.readData(self.path, 'Sheet1', i, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_tile = self.driver.title
            exp_title = 'Guru99 Bank Manager HomePage'
            lst_status = []
            if act_tile==exp_title:
                if self.exp == 'Pass':
                    self.logger.info('***********Passed********')
                    lst_status.append('Pass')
                    self.lp.clickLogout()
                    self.driver.switch_to.alert.accept()
                elif self.exp=='Fail':
                    self.logger.error('***********Failed********')
                    lst_status.append('Fail')
                    self.lp.clickLogout()
                    self.driver.switch_to.alert.accept()
            elif act_tile!=exp_title:
                if self.exp == 'Pass':
                    self.driver.switch_to.alert.accept()
                    self.logger.error('***********Failed********')
                    lst_status.append('Fail')
                elif self.exp=='Fail':
                    self.driver.switch_to.alert.accept()
                    self.logger.info('***********Passed********')
                    lst_status.append('Pass')
        if 'Fail' not in lst_status:
            self.logger.info('************Login DDT Test Passed***********')
            assert True
        else:
            self.logger.info('************Login DDT Test Fail***********')
            assert False

        self.driver.close()
        self.logger.info('************Login DDT Test End***********')
if __name__=='__main__':
    pytest.main(['-v','test_eBankLogin.py'])
