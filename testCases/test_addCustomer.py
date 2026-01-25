import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddcutomerPage import AddCustomer
import string
import random



class Test_003_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()   #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************** Test _003_AddCustomer *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.username = self.username
        self.lp.password = self.password
        self.lp.clickLogin()

        self.logger.info("************** Login Successful ***************")

        self.logger.info("************** Starting Add Customer Test ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("************** Providing customer info ***************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("Google")
        self.addcust.setIsTaxExempt()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendoor("Vendoor 2")
        self.addcust.setCheckboxActive()
        self.addcust.setCustomerMustChangePassword()
        self.addcust.setAdminComment("Thank You")

        self.addcust.clickOnSave()

        self.logger.info("*************** Save Customer Information ***************")

        self.logger.info("*************** Add Customer Validation ***************")

        self.msg =self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*************** Add Customer Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")      #Screeshot
            self.logger.info("*************** Add Customer Test Failed ***************")
            assert True == False

        self.driver.close()
        self.logger.info("*************** Ending Home Page Title Test ***************")

def random_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



