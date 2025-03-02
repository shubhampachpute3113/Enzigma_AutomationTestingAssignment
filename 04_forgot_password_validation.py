from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from locators import forgot_password
from data import url, forgot_pwd_data
import gettext
import pytest

def open_browser():
    service = Service(os.path.join(os.getcwd(), "chromedriver.exe"))
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    return driver

def test_valid_registered_email():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, forgot_password['forgot_password_link'])))
    driver.find_element(By.XPATH, forgot_password['forgot_password_link']).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, forgot_password['email_xpath'])))
    driver.find_element(By.XPATH, forgot_password['email_xpath']).send_keys(forgot_pwd_data["email"])

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, forgot_password['proceed_btn'])))
    driver.find_element(By.XPATH, forgot_password['proceed_btn']).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, forgot_password["toast_alert_msg_xpath"])))
    alert_msg = driver.find_element(By.XPATH, forgot_password["toast_alert_msg_xpath"]).text
    assert "Verification code sent successfully" in alert_msg

def test_invalid_non_registered_email():
    driver = open_browser()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, forgot_password['forgot_password_link'])))
    driver.find_element(By.XPATH, forgot_password['forgot_password_link']).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, forgot_password['email_xpath'])))
    driver.find_element(By.XPATH, forgot_password['email_xpath']).send_keys(forgot_pwd_data["email_non_registered"])

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, forgot_password['proceed_btn'])))
    driver.find_element(By.XPATH, forgot_password['proceed_btn']).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, forgot_password["toast_alert_msg_xpath"])))
    alert_msg = driver.find_element(By.XPATH, forgot_password["toast_alert_msg_xpath"]).text
    assert "User does not exists" in alert_msg

def test_blank_email():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, forgot_password['forgot_password_link'])))
    driver.find_element(By.XPATH, forgot_password['forgot_password_link']).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, forgot_password['email_xpath'])))
    driver.find_element(By.XPATH, forgot_password['email_xpath']).send_keys('')

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, forgot_password['proceed_btn'])))
    driver.find_element(By.XPATH, forgot_password['proceed_btn']).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, forgot_password["toast_alert_msg_xpath"])))
    alert_msg = driver.find_element(By.XPATH, forgot_password["toast_alert_msg_xpath"]).text
    assert "Please enter email" in alert_msg

def test_invalid_email_format():
    driver = open_browser()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, forgot_password['forgot_password_link'])))
    driver.find_element(By.XPATH, forgot_password['forgot_password_link']).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, forgot_password['email_xpath'])))
    driver.find_element(By.XPATH, forgot_password['email_xpath']).send_keys(forgot_pwd_data["email_invalid_format"])

    alert_msg = driver.find_element(By.XPATH, forgot_password['invalid_email_alert']).text
    assert alert_msg=="Please enter a valid email"

if __name__ == '__main__' :
    test_valid_registered_email()
    test_invalid_email_format()
    test_invalid_non_registered_email()
    test_blank_email()
