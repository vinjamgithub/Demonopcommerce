# from lib2to3.pgen2 import driver
from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By

from POM.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from POM.Addcustomerpage import Addcustomer
import string
import random


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_Addcustomer:
    baseURL = ReadConfig.getapplicationURL()
    Email = ReadConfig.getEmail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self, setup):
        self.logger.info("***** Test_003_Addcustomer ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setEmail(self.Email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** login sucessfully ****")

        self.logger.info("**** started addcustomer ****")
        self.logger.info("**** providing customer info ****")

        self.addcust = Addcustomer(self.driver)
        self.addcust.clickoncustomermenu()
        time.sleep(2)
        self.addcust.clickoncustomersubmenu()
        self.addcust.clickonadd()

        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        print(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setfstname("john")
        self.addcust.setlstname("kevin")
        self.addcust.selectgender("Male")
        self.addcust.setdob("7/05/1995")
        self.addcust.setcmpname("TATA")
        #self.TNI = self.addcust.setTni("NTR")
        # self.addcust.custmrole("Guests")
        self.addcust.setmov("Vendor 2")
        self.addcust.setadmin("this is for testing...")
        self.addcust.clickonsave()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_png1.png")
        self.logger.info("*** customer info is saved ****")

        self.logger.info("**** customer validations is started ****")

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        time.sleep(2)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("**** customer is passed ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_png.png")
            self.logger.info("****** customer is failed *******")
            assert True == False

        self.driver.close()
        self.logger.info("**** ending addcustomer test ****")


