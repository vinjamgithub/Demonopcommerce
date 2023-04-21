import pytest
from selenium import webdriver
from POM.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getapplicationURL()
    Email = ReadConfig.getEmail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setup):

        self.logger.info("****** Test_001_Login *******")
        self.logger.info("****** verify homepage Title *******")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.logger.info(act_title)
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** home page title is passed *******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error ("****** home page title is failed *******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.Email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****** Login test is passed *******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("****** Login test is failed *******")
            assert False
