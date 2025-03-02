from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import signup
from data import url, signup_data


def open_browser():
    service = Service(os.path.join(os.getcwd(), "chromedriver.exe"))
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    return driver

def test_valid_input():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup['sign_btn'])))
    driver.find_element(By.XPATH, signup['sign_btn']).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup["email_input"])))
    driver.find_element(By.XPATH, signup["email_input"]).send_keys(signup_data["email"])

    driver.find_element(By.XPATH,signup['t_and_c_checkbox']).click()
    driver.find_element(By.XPATH, signup["proceed_btn"]).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'code')))
    driver.find_element(By.NAME, 'code').click()
    code_text = driver.find_element(By.NAME, 'code')
    driver.implicitly_wait(5)
    ActionChains(driver).move_to_element(code_text).send_keys(input("Enter OTP: ")).perform()

    driver.find_element(By.NAME, 'verifyCode').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    fname =driver.find_element(By.NAME, 'firstName')
    ActionChains(driver).move_to_element(fname).send_keys(signup_data["fname_val"]).perform()

    lname = driver.find_element(By.XPATH, signup['lname'])
    lname.send_keys(signup_data["lname_val"])

    password = driver.find_element(By.XPATH, signup["password"])
    password.send_keys(signup_data["password"])

    confirm_password = driver.find_element(By.XPATH,signup["confirm_password"])
    confirm_password.send_keys(signup_data["confirm_password"])

    driver.find_element(By.XPATH, signup["register_btn"]).click()
    # while(True):
    #     pass

    # driver.find_element(By.XPATH, signup["cancel_btn"]).click()
    # driver.quit()

def test_invalid_email_format():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup['sign_btn'])))
    driver.find_element(By.XPATH, signup['sign_btn']).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup["email_input"])))
    driver.find_element(By.XPATH, signup["email_input"]).send_keys(signup_data["email_invalid_format"])
    alert_txt = driver.find_element(By.XPATH, signup["invalid_email_msg"]).text
    assert alert_txt=="Please enter a valid email"
    driver.quit()

def test_password_mismatch():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup['sign_btn'])))
    driver.find_element(By.XPATH, signup['sign_btn']).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup["email_input"])))
    driver.find_element(By.XPATH, signup["email_input"]).send_keys(signup_data["email"])

    driver.find_element(By.XPATH, signup['t_and_c_checkbox']).click()
    driver.find_element(By.XPATH, signup["proceed_btn"]).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'code')))
    driver.find_element(By.NAME, 'code').click()
    code_text = driver.find_element(By.NAME, 'code')
    driver.implicitly_wait(5)
    ActionChains(driver).move_to_element(code_text).send_keys(input("Enter OTP: ")).perform()

    driver.find_element(By.NAME, 'verifyCode').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    fname = driver.find_element(By.NAME, 'firstName')
    ActionChains(driver).move_to_element(fname).send_keys(signup_data["fname_val"]).perform()

    lname = driver.find_element(By.XPATH, signup['lname'])
    lname.send_keys(signup_data["lname_val"])

    password = driver.find_element(By.XPATH, signup["password"])
    password.send_keys(signup_data["password"])

    confirm_password = driver.find_element(By.XPATH, signup["confirm_password"])
    confirm_password.send_keys(signup_data["confirm_password_mismatch"])
    alert_msg = driver.find_element(By.XPATH, signup["mismatch_password_msg"]).text
    assert alert_msg == "The password and confirmation password do not match."

def test_missing_mandatory_field():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup['sign_btn'])))
    driver.find_element(By.XPATH, signup['sign_btn']).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup["email_input"])))
    driver.find_element(By.XPATH, signup["email_input"]).send_keys(signup_data["email"])

    driver.find_element(By.XPATH, signup['t_and_c_checkbox']).click()
    driver.find_element(By.XPATH, signup["proceed_btn"]).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'code')))
    driver.find_element(By.NAME, 'code').click()
    code_text = driver.find_element(By.NAME, 'code')
    driver.implicitly_wait(5)
    ActionChains(driver).move_to_element(code_text).send_keys(input("Enter OTP: ")).perform()

    driver.find_element(By.NAME, 'verifyCode').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, signup['lname'])))
    lname = driver.find_element(By.XPATH, signup['lname'])
    lname.send_keys(signup_data["lname_val"])
    alert_msg = driver.find_element(By.XPATH, signup["fname_msg"]).text
    assert alert_msg == "This field is required"

def test_invalid_special_char_in_name():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup['sign_btn'])))
    driver.find_element(By.XPATH, signup['sign_btn']).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, signup["email_input"])))
    driver.find_element(By.XPATH, signup["email_input"]).send_keys(signup_data["email"])

    driver.find_element(By.XPATH, signup['t_and_c_checkbox']).click()
    driver.find_element(By.XPATH, signup["proceed_btn"]).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'code')))
    driver.find_element(By.NAME, 'code').click()
    code_text = driver.find_element(By.NAME, 'code')
    driver.implicitly_wait(5)
    ActionChains(driver).move_to_element(code_text).send_keys(input("Enter OTP: ")).perform()

    driver.find_element(By.NAME, 'verifyCode').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    fname = driver.find_element(By.NAME, 'firstName')
    ActionChains(driver).move_to_element(fname).send_keys(signup_data["fname_special_char"]).perform()
    alert_msg = driver.find_element(By.XPATH, signup["fname_msg"]).text
    assert alert_msg=="Special characters are not allowed"



if __name__ == '__main__' :
    test_invalid_email_format()
    test_password_mismatch()
    test_missing_mandatory_field()
    test_invalid_special_char_in_name()
    test_valid_input()
