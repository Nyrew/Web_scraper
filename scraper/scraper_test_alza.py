import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#from .config import URL, XPATH_PRODUCT_ITEM, XPATH_PRODUCT_NAME, XPATH_PRODUCT_PRICE

CHROMEDRIVER_PATH = "./chromedriver/chromedriver"
urls = [
    "https://www.alza.cz/macbook-air-15-m3-cz-2024-vesmirne-sedy-d10866091.htm",
    "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=10931503",
    "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=12283509",
    "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=10931532"
]

def scrape():
    try:
        service = Service(executable_path=CHROMEDRIVER_PATH)
        chrome_options = Options()
         # Headless nastavení
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--start-maximized')
        
        # Přidání User-Agent
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        for url in urls:
            
            driver.get(url)
        
            wait = WebDriverWait(driver, 10)
            
            # Název produktu - použijeme span uvnitř div class="nameextc"
            name = wait.until(
                
                EC.presence_of_element_located((By.XPATH, "//div[@class='nameextc']//span"))
            ).text
            print(f"Název produktu: {name}")
            
            # Cena produktu - použijeme span s class="price-box__price-text"
            price = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-detail__price-box-wrapper js-price-detail__main-price-box-wrapper']//span[@class='price-box__price']"))
            ).text
            print(f"Cena produktu: {price}")
        
    except Exception as e:
        print(f"Došlo k chybě: {e}")
        return None
        
    finally:
        driver.quit()


if __name__ == "__main__":
    scrape()