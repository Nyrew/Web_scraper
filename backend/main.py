from fastapi import FastAPI
from scraper.config import *
from scraper.scraper import scrape
from database.database import get_db, engine, DATABASE_URL
from database.models import Base, Product
from database.crud import save_scraped_data, get_all_data
from datetime import datetime
import psycopg2

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
    
    

@app.get("/test-selenium")
def test_scrape():
    scraped_data_istyle = scrape(
            CONFIG_ISTYLE,
            XPATH_PRODUCT_NAME_ISTYLE,
            XPATH_PRODUCT_PRICE_ISTYLE,
            XPATH_COOKIES_BUTTON_ISTYLE
        )
    print(scraped_data_istyle)
    return {"status": "success", "data": scraped_data_istyle}


@app.get("/test")
def test():
    text = "This is working22"
    return text

@app.get("/add")
def add_product():
    new_product = Product(
        shop="Example Shop",
        product_name="Example Product",
        product_id=123456,
        price=999.99,
        url="https://example.com/product/123456",
        ram="16GB",
        gpu="NVIDIA GTX 3080",
        ssd="512GB",
        date=datetime.now()
    )

    try:
        db = next(get_db())
        db.add(new_product)
        db.commit()
        print("New product added successfully!")
    except Exception as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()

@app.get("/get")
def fetch_all_data():
    try:
        # Připojení k databázi
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # SQL dotaz pro výběr všech dat
        query = "SELECT * FROM products;"  # Přizpůsobte název tabulky
        cursor.execute(query)

        # Načtení všech řádků
        rows = cursor.fetchall()

        # Vypsání dat do konzole
        for row in rows:
            print(row)

        # Zavření kurzoru a spojení
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error:", e)