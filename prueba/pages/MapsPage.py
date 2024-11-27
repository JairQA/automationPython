from pages.BasePage  import BasePage
from selenium.webdriver.common.by import By

class MapsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
 
    #locator register
    RegisterBtn = (By.XPATH, "//*[text()=' Sign up ']")
    nameTxt = (By.ID, "full-name")
    mailTxt = (By.ID, "email")
    passwordTxt = (By.XPATH, "//input[@id='password']")
    passwor2dTxt = (By.XPATH, "//input[@id='confirm-password']")
    signinBtn = (By.CSS_SELECTOR, 'button[type="submit"]')
    successfulRegister= (By.XPATH, "//div[text()='Successful registration!']")
    popup= (By.XPATH,'//button[contains(@aria-label, "Close")]')
    #locator Login
    mailLoginTxt = (By.ID, "email")
    mailPassTxt = (By.CSS_SELECTOR, 'input.input.input-bordered[type="password"][id="password"]')
    loginBtn = (By.XPATH, '//button[contains(text(), "Sign in")]')
    nameUserTxt = (By.XPATH, '//h2[@class="font-bold"]')
    menuBtn = (By.XPATH, '//label[@class="btn btn-ghost btn-circle avatar"]')
    logoutBtn = (By.XPATH, '//a[text()="Logout"]')