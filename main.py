import json
from scraper.config import *
from scraper.scraper import scrape
from database.db_model import engine, Base
from sqlalchemy.orm import sessionmaker
from save_data_to_dtb import save_product_data, get_all_data
    
def load_data_from_json(file_path):
    """Načte data ze souboru JSON."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":    
    results_istyle = scrape(CONFIG_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
    #result_alza = scrape(CONFIG_ALZA, XPATH_PRODUCT_NAME_ALZA, XPATH_PRODUCT_PRICE_ALZA)
    print(results_istyle)
    #print(result_alza)
    

    
    for result in results_istyle:
        save_product_data(result)
        
    get_all_data()
    
    #data = load_data_from_json("data/data.json")
    
    #for item in data:
    #    print(f"Obchod: {item['shop']}, Název produktu: {item['name']}, Cena: {item['price']}")
    