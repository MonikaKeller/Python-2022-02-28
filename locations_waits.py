from selenium import webdriver
from selenium.webdriver.common.by import By

class table_has_rows:

    def __init__(self, number):
        self.number = number

    def __call__(self, driver: webdriver.Chrome):    
        rows = driver.find_elements(By.CSS_SELECTOR, "#locations-table-tbody > tr")
        return len(rows) == self.number