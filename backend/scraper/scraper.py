from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

def scrape_single(
    configs: dict, 
    xpath_product_price: str, 
    xpath_cookies_button: str = None)  -> dict:
    """
    Scrapes product information from Alza using provided configuration.
    
    Args:
        configs (list): List of dictionaries containing product configurations
        xpath_price (str): XPath for product price element
        xpath_cookies (str, optional): XPath for cookies button
        
    Returns:
        list: List of dictionaries containing scraped data with specifications
    """
    
    updated_configs: list = configs.copy()
    cookie_clicked: bool = False
    
    # Selenium Grid URL (replace with your actual Docker/Selenium Grid URL)
    #selenium_url = "https://docker-selenium-swt8.onrender.com/wd/hub"  # Remote WebDriver URL

    #service = Service(executable_path=CHROMEDRIVER_PATH)
    
    service = Service(executable_path=os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver"))
    
    chrome_options = Options()
    
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    chrome_options.binary_location = os.getenv("CHROMIUM_PATH", "/usr/bin/chromium")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)  

    for config in updated_configs:
        try:
            driver.get(config['url'])
            
            if xpath_cookies_button and not cookie_clicked:
                try:
                    wait = WebDriverWait(driver, 2)
                    cookie_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, xpath_cookies_button))
                    )
                    cookie_button.click()
                    cookie_clicked = True
                except Exception as e:
                    print(f"Failed to click cookies button: {e}")

            price = driver.find_element(By.XPATH, xpath_product_price).text
            #print(f"Product price: {price}")
            
            config['price'] = price#.replace(',-', '').replace('Kč', '').replace(' ', '')
            
        except Exception as e:
            print(f"Error occurred while scraping: {e}")
    
    driver.quit()
    return updated_configs

def scrape_parallel(configs, price_xpath, xpath_cookies_button=None):
    def scrape_wrapper(config):
        return scrape_single([config], price_xpath, xpath_cookies_button)
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(scrape_wrapper, configs))
    return results