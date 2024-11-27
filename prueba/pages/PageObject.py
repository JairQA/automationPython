from pages.MapsPage import MapsPage
import time
class PageObjectHome(MapsPage):
        def __init__(self, driver):
            super().__init__(driver)

        def loadUrl(self,url): 
              self.driver.get(url)
              self.driver.maximize_window()
#realizar el registro
        def registration(self,nameUser,mailUser,passworduser):
                time.sleep(5)
                self.click_element(MapsPage.RegisterBtn)
                self.send_keys(MapsPage.nameTxt,nameUser)
                self.send_keys(MapsPage.mailTxt,mailUser)
                time.sleep(5)
                self.send_keys(MapsPage.passwordTxt,passworduser)
                self.send_keys(MapsPage.passwor2dTxt,passworduser)
                self.click_element(MapsPage.signinBtn)
                time.sleep(1)
#realizar el login
        def login_user(self, mailUser, password): 
                self.send_keys(MapsPage.mailLoginTxt, mailUser)
                self.send_keys(MapsPage.mailPassTxt, password)
                self.click_element(MapsPage.loginBtn)
                time.sleep(3)
                
#validar registro exitoso
        def successful_registration(self):
               text=self.get_text(MapsPage.successfulRegister)
               return text
#cerrar pop up
        def close_popup(self): 
                self.click_element(MapsPage.popup)
#cerrar sesión
        def logout_user(self):
                self.click_element(MapsPage.menuBtn)
                time.sleep(3)
                self.click_element(MapsPage.logoutBtn)   
                time.sleep(5)

        def get_name(self):
               user_name = self.get_text(MapsPage.nameUserTxt)
               return user_name                 
                
         
         