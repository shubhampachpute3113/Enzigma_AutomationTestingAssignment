from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
def test_load_page():
    service = Service(os.path.join(os.getcwd(), "chromedriver.exe"))
    driver = webdriver.Chrome(service=service)
    driver.get("https://app-staging.nokodr.com/")
    driver.quit()

if __name__ == '__main__' :
    test_load_page()
