from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selenium_url = "https://docker-selenium-swt8.onrender.com/wd/hub"  # Adresa Selenium Grid

chrome_options = Options()
chrome_options.add_argument("--headless")  # Pro headless režim

capabilities = DesiredCapabilities.CHROME.copy()

# Připojení k Remote WebDriveru
driver = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities=capabilities,
    options=chrome_options
)

driver.get("http://google.com")
print(driver.title)
driver.quit()
