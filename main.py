import json
from scraper.config import (
    URL_ISTYLE, 
    XPATH_PRODUCT_ITEM_ISTYLE, 
    XPATH_PRODUCT_NAME_ISTYLE, 
    XPATH_PRODUCT_PRICE_ISTYLE,
    XPATH_COOKIES_BUTTON_ISTYLE
)
from scraper.scraper import scrape
    
def load_data_from_json(file_path):
    """Načte data ze souboru JSON."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    scrape(URL_ISTYLE, XPATH_PRODUCT_ITEM_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
    data = load_data_from_json("data/data.json")
    
    for item in data:
        print(f"Název produktu: {item['name']}, Cena: {item['price']}")
    