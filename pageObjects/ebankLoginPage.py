from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    text_uid_xpath="//input[@name='uid']"
    text_password_xpath="//input[@name='password']"
    button_login_xpath="//input[@name='btnLogin']"
    link_logout_linktext='Log out'

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username='mngr588680'):
        self.driver.find_element(By.XPATH,self.text_uid_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_uid_xpath).send_keys(username)

    def setPassword(self,password='tUhAnUm'):
        self.driver.find_element(By.XPATH,self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()