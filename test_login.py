from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import pytest
from test_data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    os.environ['PATH'] += "D:/selenium"
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_without_entering_any_data(setup):

    driver = setup
    driver.get("https://www.vietnamairlines.com/")
    wait = WebDriverWait(driver, 10)
    cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'cookie-agree')))
    cookie_button.click()

    login_btn = driver.find_element(By.CLASS_NAME, 'txtMemberLogin')
    login_btn.click()

    login_submit = driver.find_element(By.ID, 'btnLogin')
    login_submit.click()

    mess = driver.find_element(By.CLASS_NAME, 'formErrorContent')

    assert mess.text.split("* ")[1] == 'Trường này bắt buộc'


def test_login_without_username(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/")
    
    login_btn = driver.find_element(By.CLASS_NAME, 'txtMemberLogin')
    login_btn.click()

    username = driver.find_element(By.ID, 'lotusmileLoginAcc')
    username.send_keys("jonh123")

    login_submit = driver.find_element(By.ID, 'btnLogin')
    login_submit.click()

    mess = driver.find_element(By.CLASS_NAME, 'formErrorContent')

    assert mess.text.split("* ")[1] == 'This field is required'

def test_login_without_password(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/")
    
    login_btn = driver.find_element(By.CLASS_NAME, 'txtMemberLogin')
    login_btn.click()

    username = driver.find_element(By.ID, 'lotusmileLoginPass')
    username.send_keys("john123")

    login_submit = driver.find_element(By.ID, 'btnLogin')
    login_submit.click()

    mess = driver.find_element(By.CLASS_NAME, 'formErrorContent')

    assert mess.text.split("* ")[1] == 'This field is required'

def test_login_with_invalid_credentail(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/")
    driver.implicitly_wait(5)
    
    login_btn = driver.find_element(By.CLASS_NAME, 'txtMemberLogin')
    login_btn.click()

    username = driver.find_element(By.ID, 'lotusmileLoginAcc')
    username.send_keys("john123")

    password = driver.find_element(By.ID, 'lotusmileLoginPass')
    password.send_keys("123")

    login_submit = driver.find_element(By.ID, 'btnLogin')
    login_submit.click()

    mess = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/div[1]/div[1]/ul/div[1]/div/div[2]/div/div/div[2]/div')

    assert mess.text == ' Your login information is incorrect'

