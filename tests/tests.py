import requests

url = "https://web-scraper-ihnl.onrender.com/scrape"
#url = "https://docker-selenium-swt8.onrender.com/test-selenium" # docker - render
#url = "http://localhost:8000/scrape" # docker - local

try:
    response = requests.get(url)
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