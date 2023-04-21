from selenium.webdriver.common.by import By


class searchcustomer:
    txtemail_xpath = "//input[@id='SearchEmail']"
    txtfname_xpath = "//input[@id='SearchFirstName']"
    txtlname_xpath = "//input[@id='SearchLastName']"
    butnsearch_xpath = "//button[@id='search-customers']"

    table_xpath = "//table/tbody"
    tablerow_xpath = "//table/tbody/tr"
    tablecolu_xpath = "//table/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.txtemail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtemail_xpath).send_keys(email)

    def setfname(self, fname):
        self.driver.find_element(By.XPATH, self.txtfname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtfname_xpath).send_keys(fname)

    def setlname(self, lname):
        self.driver.find_element(By.XPATH, self.txtlname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtlname_xpath).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.butnsearch_xpath).click()

    def getnorows(self):
        return len(self.driver.find_element(By.XPATH, self.tablerow_xpath))

    def getnocolu(self):
        return len(self.driver.find_element(By.XPATH, self.tablecolu_xpath))

    def searchcustomerebyemail(self, email):
        flag = False
        for r in range(1, self.getnorows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table/tbody/tr[1]/td[2]")
            if emailid == email:
                flag = True
                break
            return flag

    def searchcustomerbyname(self, Name):
        flag = False
        for r in range(1, self.getnorows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[3]")
            if name == Name:
                flag = True
                break
            return flag


