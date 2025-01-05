from fastapi import FastAPI
from scraper.config import *
from scraper.scraper import scrape
from database.database import get_db, engine
from database.models import Base
from database.crud import save_scraped_data, get_all_data

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.post("/scrape")
def scrape_data():
    try:
        db = next(get_db())
        
        scraped_data_istyle = scrape(
            CONFIG_ISTYLE,
            XPATH_PRODUCT_NAME_ISTYLE,
            XPATH_PRODUCT_PRICE_ISTYLE,
            XPATH_COOKIES_BUTTON_ISTYLE
        )
        scraped_data_alza = scrape(
            CONFIG_ALZA,
            XPATH_PRODUCT_NAME_ALZA,
            XPATH_PRODUCT_PRICE_ALZA
        )
        for item in scraped_data_istyle, scraped_data_alza:
            save_scraped_data(db, item)
        return {"status": "success", "message": "Data byla úspěšně uložena."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/products")
def get_products():
    try:
        db = next(get_db())
        products = get_all_data(db)
        return {"status": "success", "data": products}
    except Exception as e:
        return {"status": "error", "message": str(e)}