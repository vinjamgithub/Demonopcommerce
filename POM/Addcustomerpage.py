import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Addcustomer:
    lnkcustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkcustomers_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnaddmenu_xpath = "//a[@class='btn btn-primary']"
    txtemail_xpath = "//input[@id='Email']"
    txtpassword_xpath = "//input[@id='Password']"
    txtfstname_xpath = "//input[@id='FirstName']"
    txtlastname_xpath = "//input[@id='LastName']"
    radmale_xpath = "//input[@id='Gender_Male']"
    txtdob_xpath = "//input[@id='DateOfBirth']"
    txtcompname_xpath = "//input[@id='Company']"
    txttni_xpath = "//input[@id='customer_attribute_1']"
    check_xpath = "//input[@id='IsTaxExempt']"
    txtnewlet_xpath = "(//div[@class='k-widget k-multiselect k-multiselect-clearable'])[1]"
    slctcustomer_xpath = "(//div[@class='k-widget k-multiselect k-multiselect-clearable'])[2]"
    lstitemsadmin_xpath = "//option[contains(text(),'Administrators')]"
    lstforum_xpath = "//option[contains(text(),'Forum Moderators')]"
    lstguest_xpath = "//option[contains(text(),'Guests')]"
    lstreg_xpath = "//option[contains(text(),'Registered')]"
    lstvend_xpath = "//option[contains(text(),'Vendors')]"
    drpvendor_xpath = "//select[@id='VendorId']"
    txtadmin_xpath = "//textarea[@id='AdminComment']"
    buttonsave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_menu_xpath).click()

    def clickoncustomersubmenu(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_submenu_xpath).click()

    def clickonadd(self):
        self.driver.find_element(By.XPATH, self.btnaddmenu_xpath).click()

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.txtemail_xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.txtpassword_xpath).send_keys(password)

    def setfstname(self, fname):
        self.driver.find_element(By.XPATH, self.txtfstname_xpath).send_keys(fname)

    def setlstname(self, lname):
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).send_keys(lname)

    def selectgender(self, gender):
        self.driver.find_element(By.XPATH, self.radmale_xpath).click()

    def setdob(self, dob):
        self.driver.find_element(By.XPATH, self.txtdob_xpath).send_keys(dob)

    def setcmpname(self, cmpname):
        self.driver.find_element(By.XPATH, self.txtcompname_xpath).send_keys(cmpname)

    def setTni(self, tni):
        if self.txttni_xpath:
            self.driver.find_element(By.XPATH, self.txttni_xpath).send_keys(tni)
        else:
            self.setmov()


    def custmrole(self, role):
        self.driver.find_element(By.XPATH, self.slctcustomer_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstreg_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemsadmin_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstforum_xpath)
        elif role == 'Guests':
            time.sleep(4)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            time.sleep(3)
            self.listitem = self.driver.find_element(By.XPATH, self.lstguest_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstvend_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstguest_xpath)

        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setmov(self, value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpvendor_xpath))
        drp.select_by_visible_text(value)

    def setadmin(self, content):
        self.driver.find_element(By.XPATH, self.txtadmin_xpath).send_keys(content)

    def clickonsave(self):
        self.driver.find_element(By.XPATH, self.buttonsave_xpath).click()


