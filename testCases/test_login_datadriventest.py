import time
from operator import truediv

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
import time

@pytest.mark.serial
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".\\TestData\\LoginData.xlsx"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()



    def test_login_ddt(self, setup):
        self.logger.info("*************** Test_002_DDT_Login ***************")
        self.logger.info("************** Verifying Login DDT test *******************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a excel file:",self.rows)

        lst_status = []   #Empty list Variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()


            #####chatgpt for some popups show
            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                print("Handling Alert:", alert_text)
                alert.accept()
            except NoAlertPresentException:
                pass
            except UnexpectedAlertPresentException:
                pass           #####chatgpt for some popups show
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************** passed ***************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("************** failed ***************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("************** failed ***************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("************** Passed ***************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("******* Login DDT test passed ***********")
            self.driver.close()
            assert True

        else:
            self.logger.info("*************** Login DDT test failed ************")
            self.driver.close()
            assert False

        self.logger.info("*************** End of login DDT test *************")
        self.logger.info("*************** Completed TC_LoginDDT_002 *************")