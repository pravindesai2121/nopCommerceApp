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



class Test_searchCustomerByEmail_004_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()   #Logger


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************** SearchCustomerByEmail_004 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.username = self.username
        time.sleep(3)
        self.lp.password = self.password
        time.sleep(3)
        self.lp.clickLogin()

        self.logger.info("************** Login Successful ***************")

        self.logger.info("************** Starting Search Customer By Email ***************")



        self.addcust = AddCustomer(self.driver)
        self.addcust.close_info_popup(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("************** Search Customer By EmailID ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("************** Search Customer By EmailID_004 Finished ***************")
        self.driver.close()