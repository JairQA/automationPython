from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
       
    def start_driver():
      driver = webdriver.Chrome()
      driver.maximize_window()
      return driver

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def visible_element(driver, locator, time):
     try:
        wait = WebDriverWait(driver, time)
        wait.until(EC.visibility_of_element_located(locator))
        return True
     except Exception as ex:
        return False
     
    def get_text(self, locator):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return text
#time wait
    def time_wait(self,time):
         wait = WebDriverWait(self.driver, time)
         
            
         
         

