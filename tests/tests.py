import requests

url = "https://scraper-selenium.onrender.com/test-selenium"
#url = "http://localhost:8000/scrape"

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