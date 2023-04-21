from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By

from POM.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from POM.Addcustomerpage import Addcustomer
from POM.SearchCustomerPage import searchcustomer
import string
import random

class Test_004_searchcustomer:
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

        self.logger.info("**** searching customer **** ")
        searchcust = searchcustomer(self.driver)
        searchcust.setemail("kiyjcycyhjc676008@gmail.com")
        searchcust.clicksearch()
        '''time.sleep(7)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_searchcustomer_png1.png")
        status = searchcust.searchcustomerebyemail("kiyjcycyhjc676008@gmail.com")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_searchcustomer_png2.png")
        assert True == status
        self.logger.info("**** searching is customer is finished **** ")
        self.driver.close()
      '''