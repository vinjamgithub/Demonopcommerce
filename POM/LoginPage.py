from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_Email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, Email):
        self.driver.find_element(By.ID, self.textbox_Email_id).clear()
        self.driver.find_element(By.ID, self.textbox_Email_id).send_keys(Email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
