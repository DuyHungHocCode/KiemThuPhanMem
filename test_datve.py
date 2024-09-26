from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import pytest
from test_data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

def test_checkMaxpsg(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/vn/vi/home")

    wait = WebDriverWait(driver, 10)
    cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'cookie-agree')))
    cookie_button.click()
    
    open_ticket = driver.find_element(By.ID, 'city-to-roundtrip')
    open_ticket.click()

    Passenger = driver.find_element(By.ID, 'txtRoundTripPassenger')
    Passenger.click()

    psg_increase = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[1]/div[2]/button[2]')
    for _ in range(0, 9):
        psg_increase.click()

    kid_2_12 = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[2]/div[2]/button[2]')

    if kid_2_12.get_attribute("disabled") or not kid_2_12.is_enabled():
        assert True, "Test passed:"
    else:
        pytest.fail()

def test_checkMaxpsg1(setup):
    driver = setup
    kid_under_2 = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[3]/div[2]/button[2]')
    for _ in range(0, 9):
        kid_under_2.click()

    numberOfKids = driver.find_element(By.ID, 'current_passenger_infant')

    assert numberOfKids.text == '9'

def test_checkMaxpsg2(setup):
    driver = setup
    psg_decrease = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[1]/div[2]/button[1]')
    for _ in range(0, 9):
        psg_decrease.click()

    numberOfKids = driver.find_element(By.ID, 'current_passenger_infant')

    assert numberOfKids.text == '1'

def test_checkMaxpsg3(setup):
    driver = setup
    
    data = [1, 2, 3]
    count = 0
    psg_increase = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[1]/div[2]/button[2]')
    for i in data:
        for _ in range(1, i):
            # sleep(0.5)
            psg_increase.click()
            # print(".")

        kid_under_12 = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[2]/div[2]/button[2]')  
        for _ in range(0, 2*i):
            # sleep(0.5)
            kid_under_12.click()

        current_passenger_adult = driver.find_element(By.ID, 'current_passenger_adult')
        cpa = current_passenger_adult.text
        # print(cpa)
        current_passenger_child = driver.find_element(By.ID, 'current_passenger_child')
        cpc = current_passenger_child.text
        # print(cpc)
        if 2*int(cpa) == int(cpc):
            # print("true")
            count +=1

        # print('ok')
        psg_decrease = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[1]/div[2]/button[1]')
        for _ in range(0, i):
            psg_decrease.click()

        kid_under_12decrease = driver.find_element(By.XPATH, '/html/body/form/div[9]/nav/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div[1]/div[8]/div[2]/ul/li[2]/div[2]/button[1]')  
        for _ in range(0, 2*i):
            kid_under_12decrease.click()

    assert count == 3
    

    