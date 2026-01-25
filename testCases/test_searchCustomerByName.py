import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddcutomerPage import AddCustomer
import string
import random

class Test_searchCustomerByName_005_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()   #Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************** SearchCustomerByEmail_004 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.username = self.username
        self.lp.password = self.password
        self.lp.clickLogin()

        self.logger.info("************** Login Successful ***************")

        self.logger.info("************** Starting Search Customer By Name ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("************** Search Customer By Name ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("************** Search Customer By Name_005 Finished ***************")
        self.driver.close()