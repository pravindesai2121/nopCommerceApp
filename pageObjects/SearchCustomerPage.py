from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchCustomer:
    # Search customer page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    #drpIsActive_xpath = "//select[@id='SearchIsActive']"

    clickSearchButton_xpath = "//button[@id='search-customers']"

    tblSearchResults_xpath = "//div[@class='d-md-flex justify-content-between align-items-center col-12 dt-layout-full col-md']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver



    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txtEmail_id).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_id).send_keys(email)

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH,self.txtFirstName_id).clear()
        self.driver.find_element(By.XPATH,self.txtFirstName_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH,self.txtLastName_id).clear()
        self.driver.find_element(By.XPATH,self.txtLastName_id).send_keys(lastName)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.clickSearchButton_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_element(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email==emailid:
                flag=True
                break
            return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag=True
                break
            return flag




