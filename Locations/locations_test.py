from urllib import request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

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
    driver.find_element(By.CLASS_NAME,"btn-primary").click()
    
    driver.find_element(By.ID,"location-name").send_keys("Home")
    driver.find_element(By.ID,"location-coords").send_keys("1,1")
    
    
    #Then
    #message = driver.find_element(By.ID,"message div").text
    #assert message == 'Location has been created'
    pass
