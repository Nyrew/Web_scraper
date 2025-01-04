from scraper.config import *
from scraper.scraper import scrape
from database.database import get_db
from database.crud import save_scraped_data, get_all_data, delete_all_products
from database.database import engine
from database.models import Base
from server.app import app

def create_dtb():
    Base.metadata.create_all(engine)

def print_all():
    db = next(get_db())
    x = get_all_data(db)
    for row in x:
        print(row)

def main():
    db = next(get_db())
    scraped_data_istyle = scrape(CONFIG_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
    scraped_data_alza = scrape(CONFIG_ALZA, XPATH_PRODUCT_NAME_ALZA, XPATH_PRODUCT_PRICE_ALZA)
    print("Scrape done!!")
    for item in scraped_data_istyle, scraped_data_alza:
        save_scraped_data(db, item)
    print("Data byla úspěšně uložena do databáze.")

if __name__ == "__main__":   
    #delete_all_products(next(get_db()))
    # main()
    # crea
    # te_dtb()
    # main() 
    print_all()
    app.run(debug=True)
    #results_istyle = scrape(CONFIG_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
    #result_alza = scrape(CONFIG_ALZA, XPATH_PRODUCT_NAME_ALZA, XPATH_PRODUCT_PRICE_ALZA)
    #print(results_istyle)
    #print(result_alza)
 