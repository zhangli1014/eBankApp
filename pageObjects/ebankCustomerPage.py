from selenium import webdriver
from selenium.webdriver.common.by import By

class AddCustomer:
    linkCustomer_menu_xpath="//a[text()='New Customer']"
    txtCustomerName_xpath="//input[@type='text' and @name='name']"
    radioMaleGender_xpath = "//input[@type='radio' and @value='m']"
    radioFemaleGender_xpath = "//input[@type='radio' and @value='f']"
    inputBirth_xpath = "//*[@id='dob']"
    txtAddr_xpath = "//textarea[@name='addr']"
    txtCity_xpath = "//input[@name='city']"
    txtState_xpath = "//input[@name='state']"
    txtPin_xpath = "//input[@name='pinno']"
    txtMobile_xpath = "//input[@name='telephoneno']"
    txtEmail_xpath = "//input[@name='emailid']"
    txtPass_xpath = "//input[@name='password']"
    btnSubmit_xpath = "//input[@value='Submit']"
    btnReset_xpath = "//input[@value='Reset']"

    def __init__(self,driver):
        self.driver = driver

    def clickNewCustome(self):
        self.driver.find_element(By.XPATH,self.linkCustomer_menu_xpath).click()

    def setCustomerName(self,customername):
        self.driver.find_element(By.XPATH,self.txtCustomerName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtCustomerName_xpath).send_keys(customername)

    def setGender(self,gender):
        if gender=='male':
            self.driver.find_element(By.XPATH,self.radioMaleGender_xpath).click()
        elif gender=="female":
            self.driver.find_element(By.XPATH,self.radioFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radioMaleGender_xpath).click()
    def setBirth(self,birthdata):
        self.driver.find_element(By.XPATH,self.inputBirth_xpath).clear()
        self.driver.find_element(By.XPATH, self.inputBirth_xpath).send_keys(birthdata)

    def setAddress(self,addr):
        self.driver.find_element(By.XPATH,self.txtAddr_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAddr_xpath).send_keys(addr)

    def setCity(self,city):
        self.driver.find_element(By.XPATH,self.txtCity_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCity_xpath).send_keys(city)

    def setState(self,state):
        self.driver.find_element(By.XPATH,self.txtState_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtState_xpath).send_keys(state)

    def setPin(self,pin):
        self.driver.find_element(By.XPATH,self.txtPin_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPin_xpath).send_keys(pin)

    def setMobile(self,mobile):
        self.driver.find_element(By.XPATH,self.txtMobile_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtMobile_xpath).send_keys(mobile)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPass(self,password):
        self.driver.find_element(By.XPATH,self.txtPass_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPass_xpath).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickReset(self):
        self.driver.find_element(By.XPATH,self.btnReset_xpath).click()