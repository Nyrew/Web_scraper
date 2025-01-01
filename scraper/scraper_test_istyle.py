import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from .config import URL, XPATH_PRODUCT_ITEM, XPATH_PRODUCT_NAME, XPATH_PRODUCT_PRICE

CHROMEDRIVER_PATH = "./chromedriver/chromedriver"

def scrape():
      
    service = Service(executable_path=CHROMEDRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    data = []
    
    driver.get('https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html')    
    cookie_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))
    )
    cookie_button.click()
    
    time.sleep(2)
    name = driver.find_element(by='xpath', value='//div[@class="page-title-wrapper product"]').text
    #print(f"Název produktu: {name}")

    price = driver.find_element(by='xpath', value='//div[@class="special-price"]').text
    #print(f"Cena produktu: {price}")

    data.append({"name": name, "price": price})
    
    print(data)
        
    driver.quit()


if __name__ == "__main__":
    scrape()