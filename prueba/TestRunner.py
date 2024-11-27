import pytest
from selenium import webdriver
from pages.PageObject import PageObjectHome
import time
import csv

#inicializar y cerrar el navegador
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def page(driver):
    return PageObjectHome(driver)
#leer csv
@pytest.fixture(scope="module")
def data():
    with open('data.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return next(reader) 
#validar carga de pagina correcta
def test_load_url(page):
    page.loadUrl("https://test-qa.inlaze.com/")
    assert "Inlaze - QA Test Front" in page.driver.title 
    time.sleep(5)
#validar el registro de un usario exitoso
def test_registration(page,data):
    nameUser = data['nameUser']
    mailUser = data['mailUser']
    passwordUser = data['passwordUser']
    page.registration(nameUser,mailUser,passwordUser)
    time.sleep(2)
    assert "Successful registration!" in page.successful_registration() 
    page.close_popup()
#validar el login
    
def test_login(page,data):
    nameUser = data['nameUser']
    mailUser = data['mailUser']
    passwordUser = data['passwordUser']
    page.login_user(mailUser,passwordUser)
    assert nameUser in page.get_name() 
    page.logout_user()
    
