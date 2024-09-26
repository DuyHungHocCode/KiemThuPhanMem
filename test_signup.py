from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import pytest
from test_data import *

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

def test_registration_without_entering_any_data(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/lotusmiles/enroll-new")
    cookie_agree = driver.find_element(By.ID, 'cookie-agree')
    cookie_agree.click()

    next_step = driver.find_element(By.ID, 'btnEnrollNextToStep2')
    next_step.click()

    mess = driver.find_element(By.CLASS_NAME, 'formErrorContent')

    assert mess.text.split("* ")[1] == 'Trường này bắt buộc'

def test_name_field_accepts_only_alphabetic_characters(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/lotusmiles/enroll-new")
    # cookie_agree = driver.find_element(By.ID, 'cookie-agree')
    # cookie_agree.click()

    dropdown = driver.find_element(By.ID, "selectBox_ddlLotusMilesEnrollTitleGender")
    dropdown.send_keys("Ông")

    
    Family_name = driver.find_element(By.ID, "memberLastName")
    Family_name.send_keys("Jonh123")
     
    Given_name = driver.find_element(By.ID, 'memberFirstName')
    Given_name.send_keys(valid_data['username'].split(" ")[1])

    day_field = driver.find_element(By.ID, 'enroll-birth-date')
    day_field.send_keys("20")

    month_field = driver.find_element(By.ID, 'enroll-birth-month')
    month_field.send_keys("08")

    year_field = driver.find_element(By.ID, 'enroll-birth-year')
    year_field.send_keys("2003")

    Nationality = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMemberNationality')
    Nationality.send_keys("Viet Nam")

    Preferred_Language = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMemberLanguage')
    Preferred_Language.send_keys("Vietnamese")

    next_step = driver.find_element(By.ID, 'btnEnrollNextToStep2')
    next_step.click()

    mess = driver.find_element(By.CLASS_NAME, 'formErrorContent')
    
    assert mess.text.split("* ")[1] == 'This field is required'

def test_age_under_16(setup):

    driver = setup
    driver.get("https://www.vietnamairlines.com/lotusmiles/enroll-new")
 
    dropdown = driver.find_element(By.ID, "selectBox_ddlLotusMilesEnrollTitleGender")
    dropdown.send_keys("MR")

    
    Family_name = driver.find_element(By.ID, "memberLastName")
    Family_name.send_keys("Jonh")
     
    Given_name = driver.find_element(By.ID, 'memberFirstName')
    Given_name.send_keys(valid_data['username'].split(" ")[1])

    day_field = driver.find_element(By.ID, 'enroll-birth-date')
    day_field.send_keys("20")

    month_field = driver.find_element(By.ID, 'enroll-birth-month')
    month_field.send_keys("08")

    year_field = driver.find_element(By.ID, 'enroll-birth-year')
    year_field.send_keys("2020")

    Nationality = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMemberNationality')
    Nationality.send_keys("Viet Nam")

    Preferred_Language = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMemberLanguage')
    Preferred_Language.send_keys("Vietnamese")

    next_step = driver.find_element(By.ID, 'btnEnrollNextToStep2')
    next_step.click()

    mess = driver.find_element(By.CLASS_NAME, 'msg-desc')
    
    assert mess.text == 'To enroll a Member between 2 and 16 years old, please log in to the Father or Mother Lotusmiles Account.'

def test_registration_succeed(setup):
    driver = setup
    driver.get("https://www.vietnamairlines.com/lotusmiles/enroll-new")

    dropdown = driver.find_element(By.ID, "selectBox_ddlLotusMilesEnrollTitleGender")
    dropdown.send_keys("MR")

    Family_name = driver.find_element(By.ID, "memberLastName")
    Family_name.send_keys(valid_data['username'].split(" ")[0])

    Given_name = driver.find_element(By.ID, 'memberFirstName')
    Given_name.send_keys(valid_data['username'].split(" ")[1])

    day_field = driver.find_element(By.ID, 'enroll-birth-date')
    day_field.send_keys("20")

    month_field = driver.find_element(By.ID, 'enroll-birth-month')
    month_field.send_keys("08")

    year_field = driver.find_element(By.ID, 'enroll-birth-year')
    year_field.send_keys("2003")

    Nationality = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMemberNationality')
    Nationality.send_keys("Viet Nam")

    Preferred_Language = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMemberLanguage')
    Preferred_Language.send_keys("Vietnamese")
    Preferred_Language.click()

    next_step = driver.find_element(By.ID, 'btnEnrollNextToStep2')
    next_step.click()

    Address = driver.find_element(By.ID, 'enrollAddress')
    Address.send_keys(valid_data['address'])

    Country = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollCountry')
    Country.send_keys('Viet Nam')

    State = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollCompanyRegion')
    State.send_keys("Ha Noi")

    District = driver.find_element(By.ID, 'companyCity')
    District.send_keys("Long Bien")

    Phone = driver.find_element(By.ID, 'selectBox_ddlLotusMilesEnrollMobileCountry')
    Phone.send_keys('VIET NAM [84]')

    Phone_number = driver.find_element(By.ID, 'mobileNumber')
    Phone_number.send_keys(valid_data['phone'])

    Email = driver.find_element(By.ID, 'memberEmail')
    Email.send_keys(valid_data['email'])

