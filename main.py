import json
from scraper.config import *
from scraper.scraper import scrape
    
def load_data_from_json(file_path):
    """Načte data ze souboru JSON."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    scrape(CONFIG_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
    scrape(CONFIG_ALZA, XPATH_PRODUCT_NAME_ALZA, XPATH_PRODUCT_PRICE_ALZA)
    #data = load_data_from_json("data/data.json")
    
    #for item in data:
    #    print(f"Obchod: {item['shop']}, Název produktu: {item['name']}, Cena: {item['price']}")
    