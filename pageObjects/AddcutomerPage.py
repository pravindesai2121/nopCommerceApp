import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer():
    # Add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath ="//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtCompanyName_xpath = "//input[@id='Company']"
    IsTaxExcempt_id ="IsTaxExempt"
    txtCustomerRoles_xpath = "//input[@role='searchbox']"
    lstitemAdministrators_xpath = "//li[@title='Administrators']"
    lstitemRegistered_xpath = "//li[@title='Registered']"
    lstitemGuests_xpath = "//li[@title='Guests']"
    lstitemVendors_xpath = "//li[@title='Vendors']"
    drpmgrOfVendor_xpath = "//span[@id='select2-VendorId-container']"

    CheckboxActive_xpath = "//input[@id='Active']"
    CustoomerMustChangePassword_Checkbox_xpath = "//input[@id='MustChangePassword']"
    AdminComment_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def close_info_popup(self, driver):
        try:
            close_btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".alert.alert-info .close"))
            )
            close_btn.click()
        except:
            pass  # popup not present

    def clickButtonOk(self):
        OkButton1 = self.driver.find_element(By.XPATH,"//*[@id='loadCustomerStatisticsAlert-action-alert']/div[1]/div/div[3]/span")
        OkButton1.click()
        OkButton2 = self.driver.find_element(By.XPATH,"//*[@id='loadOrderStatisticsAlert-action-alert']/div[1]/div/div[3]/span")
        OkButton2.click()


    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lastName)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(companyName)

    def setIsTaxExempt(self):
        self.driver.find_element(By.XPATH,self.IsTaxExcempt_id).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Administrator":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == "Guest":
            #Here can be use registered or guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@role='presentation'][normalize-space()='×']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click();
        self.driver.execute_script("argument[0].click();",self.listitem)

    def setManagerOfVendoor(self,value):
        drp=self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath)
        drp.select_by_visible_text(value)


    def setCheckboxActive(self):
        self.driver.find_element_by_xpath(self.CheckboxActive_xpath).click()

    def setCustomerMustChangePassword(self):
        self.driver.find_element(By.XPATH,self.CustoomerMustChangePassword_Checkbox_xpath).click()

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH,self.AdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()




