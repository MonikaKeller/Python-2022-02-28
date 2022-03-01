from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://monikakeller.github.io/Python-2022-02-28/")


header= driver.find_element(By.TAG_NAME, "h1").text
print(header)