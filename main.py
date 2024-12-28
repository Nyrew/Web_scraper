
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

web = 'https://istyle.cz/mac/macbook-air.html'
path = './chromedriver/chromedriver' 
service = Service(executable_path=path)

# Nastavení prohlížeče s loggingem
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Pokud chcete spustit Chrome bez UI (headless mód)

# Vytvoření webového ovladače
driver = webdriver.Chrome(service=service, options=chrome_options)

# Otevření webu
driver.get(web)

products = driver.find_elements(by='xpath', value='//div[contains(@class, "ais-hits--item")]')

for product in products:
    print(product.find_element(by='xpath', value='.//div[contains(@class, "product-item-name")]').text)
    print(product.find_element(by='xpath', value='.//div[contains(@class, "special-price")]').text)


# Zpoždění pro prohlédnutí stránky
#time.sleep(20)  # Počká 10 sekund než se zavře

# Zavření prohlížeče
driver.quit()
