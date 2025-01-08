import requests

#url = "https://web-scraper-ihnl.onrender.com/test-selenium"
url = "https://docker-selenium-swt8.onrender.com/scrape" # docker - render
#url = "http://localhost:8000/scrape" # docker - local

try:
    response = requests.post(url)
    response.raise_for_status()  # Vyvolá chybu, pokud HTTP status není 200
    data = response.json()
    print("Response from Render Selenium endpoint:")
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Selenium endpoint: {e}")


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/test-selenium")
# async def test_selenium():
#     return {"message": "Selenium test endpoint is working!"}

# from fastapi import FastAPI
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# app = FastAPI()

# @app.get("/test_seleniumm")
# def test_selenium():
#     selenium_url = "http://docker-selenium-swt8.onrender.com/wd/hub"
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920,1080")

#     try:
#         driver = webdriver.Remote(
#             command_executor=selenium_url,
#             options=chrome_options
#         )
#         driver.get("https://www.google.com")
#         title = driver.title
#         driver.quit()
#         return {"status": "success", "title": title}
#     except Exception as e:
        # return {"status": "error", "message": str(e)}
