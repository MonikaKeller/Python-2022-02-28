from urllib import request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

@pytest.fixture
def driver():
    # Given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # When
    driver.get("http://127.0.0.1:8080/")
    return driver

def test_create(driver:webdriver.Chrome):
    requests.delete ("http://127.0.0.1:8080/api/locations")
    driver.find_element(By.LINK_TEXT,"Create location").click()
    
    
    driver.find_element(By.ID,"location-name").send_keys("Home")
    driver.find_element(By.ID,"location-coords").send_keys("1,1")
    
    driver.find_element(By.CLASS_NAME,"btn-primary").click()
    #Then
   
    wait = WebDriverWait (driver, 3)
    wait.until(EC.text_to_be_present_in_element((By.ID,"message-div"), "Location has been created"))
    
    message = driver.find_element(By.ID,"message-div").text
    assert message == 'Location has been created'
    
    name_cell_text = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr:nth-child(1) > td:nth-child(2)").text
    
    assert name_cell_text == 'Home'
    
    name_cell_coordinate = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr > td:nth-child(3))").text
    
    assert name_cell_coordinate == '1, 1'
    pass
