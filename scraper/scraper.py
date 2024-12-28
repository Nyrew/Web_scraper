import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import URL, XPATH_PRODUCT_ITEM, XPATH_PRODUCT_NAME, XPATH_PRODUCT_PRICE

CHROMEDRIVER_PATH = "./chromedriver/chromedriver"

def scrape(): 
    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump([], file, ensure_ascii=False, indent=4)
        
    service = Service(executable_path=CHROMEDRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(URL)
    
    cookie_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))
    )
    cookie_button.click()
        
    products = driver.find_elements(by=By.XPATH, value=XPATH_PRODUCT_ITEM)

    data = []
    
    time.sleep(2)
    
    for product in products:
        name = product.find_element(by='xpath', value=XPATH_PRODUCT_NAME).text
        print(f"Název produktu: {name}")
        
        price = product.find_element(by='xpath', value=XPATH_PRODUCT_PRICE).text
        print(f"Cena produktu: {price}")
        
        data.append({"name": name, "price": price})
        
    #print(data)
        
    driver.quit()
    
    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape()