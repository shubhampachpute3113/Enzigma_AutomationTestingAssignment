from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import login
from data import url, login_data

def open_browser():
    service = Service(os.path.join(os.getcwd(), "chromedriver.exe"))
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    return driver

def test_successful_login():
    driver = open_browser()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login['login_btn_xpath'])))
    driver.find_element(By.XPATH, login["email_xpath"]).send_keys(login_data["email"])
    driver.find_element(By.XPATH, login["password_xpath"]).send_keys(login_data["password"])
    driver.find_element(By.XPATH, login["login_btn_xpath"]).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, login['login_success_xpath'])))
    driver.quit()

def test_incorrect_email():
    driver = open_browser()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login['login_btn_xpath'])))
    driver.find_element(By.XPATH, login["email_xpath"]).send_keys(login_data["invalid_email"])
    alert_msg = driver.find_element(By.XPATH, login["invalid_email_alert_xpath"]).text
    assert alert_msg=="Please enter a valid email"
    driver.quit()

def test_special_char_email():
    driver = open_browser()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login['login_btn_xpath'])))
    driver.find_element(By.XPATH, login["email_xpath"]).send_keys(login_data["special_char"])
    alert_msg = driver.find_element(By.XPATH, login["invalid_email_alert_xpath"]).text
    assert alert_msg == "Please enter a valid email"
    driver.quit()

def test_incorrect_password():
    driver = open_browser()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login['login_btn_xpath'])))
    driver.find_element(By.XPATH, login["email_xpath"]).send_keys(login_data["email"])
    driver.find_element(By.XPATH, login["password_xpath"]).send_keys(login_data["invalid_password"])
    driver.find_element(By.XPATH, login["login_btn_xpath"]).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login["toast_alert_msg_xpath"])))
    alert_msg = driver.find_element(By.XPATH, login["toast_alert_msg_xpath"]).text
    assert "Invalid Email or Password" in alert_msg
    driver.quit()

def test_blank_password():
    driver = open_browser()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login['login_btn_xpath'])))
    driver.find_element(By.XPATH, login["email_xpath"]).send_keys(login_data["email"])
    driver.find_element(By.XPATH, login["password_xpath"]).send_keys('')
    driver.find_element(By.XPATH, login["login_btn_xpath"]).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login["toast_alert_msg_xpath"])))
    alert_msg = driver.find_element(By.XPATH, login["toast_alert_msg_xpath"]).text
    assert "Please enter password" in alert_msg
    driver.quit()

if __name__ == '__main__' :
    test_successful_login()
    test_incorrect_email()
    test_special_char_email()
    test_blank_password()
    test_incorrect_password()
