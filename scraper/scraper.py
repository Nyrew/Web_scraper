from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from .config import URL, XPATH_PRODUCT_ITEM, XPATH_PRODUCT_NAME, XPATH_PRODUCT_PRICE

CHROMEDRIVER_PATH = "./chromedriver/chromedriver"

def scrape(
    configs: list, 
    xpath_product_name: str, 
    xpath_product_price: str, 
    xpath_cookies_button: str = None)  -> list:
    """
    Scrapes product information from given URLs using Selenium WebDriver.
    
    Args:
        urls (list): List of URLs to scrape from
        xpath_product_name (str): XPath expression to locate product name element
        xpath_product_price (str): XPath expression to locate product price element
        xpath_cookies_button (str, optional): XPath expression for cookies accept button. Defaults to None
        
    Returns:
        list: List of dictionaries containing scraped product data (name, price, url)
    """
    
    data: list = []
    cookie_clicked: bool = False
    
    service = Service(executable_path=CHROMEDRIVER_PATH)
    chrome_options = Options()
    
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    driver = webdriver.Chrome(service=service, options=chrome_options)   

    for config in configs:
        try:
            driver.get(config['url'])
            wait = WebDriverWait(driver, 2)
            if xpath_cookies_button and not cookie_clicked:
                try:
                    cookie_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, xpath_cookies_button))
                    )
                    cookie_button.click()
                    cookie_clicked = True
                except Exception as e:
                    print(f"Failed to click cookies button: {e}")
            
            # Get product name
            name = wait.until(
                EC.presence_of_element_located((By.XPATH, xpath_product_name))
            ).text
            print(f"Product name: {name}")
        
            # Get product price
            price = wait.until(
                EC.presence_of_element_located((By.XPATH, xpath_product_price))
            ).text
            print(f"Product price: {price}")
            
            data.append({
                "name": name,
                "price": price
            })
            
        except Exception as e:
            print(f"Error occurred while scraping: {e}")
    
    driver.quit()
    return data