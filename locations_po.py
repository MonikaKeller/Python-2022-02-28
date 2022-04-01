from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locations_waits import table_has_rows


class LocationsPage:

    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.driver.get("http://127.0.0.1:8080")   

    def click_on_create_location(self):
        self.driver.find_element(By.LINK_TEXT, "Create location").click()

    def fill_create_form(self,name,coords):
        self.driver.find_element(By.ID, "location-name").send_keys("Home")
        self.driver.find_element(By.ID, "location-coords").send_keys("1,1")

    def click_on_create_location_submit(self):
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
            
    def wait_for_message(self, message):        
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "message-div"), message))

    def wait_for_name_message(self, message):        
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "location-name-feedback"), message))

    def get_first_location_in_table(self):
        row = self.driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody" )
        name = row.find_element(By.CSS_SELECTOR, " td:nth-child(2)" ).text
        coords = row.find_element(By.CSS_SELECTOR, " td:nth-child(3)" ).text
        return(name,coords)
                
    def has_name_red_border(self):
         input_field = self.driver.find_element(By.ID, "location-name")
         return "is-invalid" in input_field.get_attribute("class").split()
        

    def wait_for_table_has_rows(self,number):
        self.wait.until(table_has_rows(number))


    def click_on_first_edit_button(self):
       self.driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr > td:nth-child(6) > button.btn.btn-link").click()

    def click_on_first_delete_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr > td:nth-child(6) > button.btn.btn-danger").click()

    def click_on_delete_location_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "[value='Delete location']").click()


    def fill_update_form(self,name,coords):
        name_field = self.driver.find_element(By.ID, "update-location-name")
        name_field.clear()
        name_field.send_keys(name)

        coords_field = self.driver.find_element(By.ID, "update-location-coords")
        coords_field.clear()
        coords_field.send_keys(coords)

    def click_on_update_location_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "[value='Update location']").click()
