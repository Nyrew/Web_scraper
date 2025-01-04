from fastapi import FastAPI
from scraper.config import *
from scraper.scraper import scrape
from database.database import get_db
from database.crud import save_scraped_data, get_all_data, delete_all_products

app = FastAPI()

@app.post("/scrape")
def scrape():
    try:
        db = next(get_db())
        scraped_data_istyle = scrape(CONFIG_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
        scraped_data_alza = scrape(CONFIG_ALZA, XPATH_PRODUCT_NAME_ALZA, XPATH_PRODUCT_PRICE_ALZA)
        print("Scrape done!!")
        for item in scraped_data_istyle, scraped_data_alza:
            save_scraped_data(db, item)
        print("Data byla úspěšně uložena do databáze.")
    except Exception as e:
       return {"status": "error", "message": str(e)} 

@app.get("/products")
def get_products():
    db = next(get_db())
    x = get_all_data(db)
    for row in x:
        print(row)

#if __name__ == "__main__":   
    #delete_all_products(next(get_db()))
    # main()
    # crea
    #create_dtb()
    # main() 
    #print_all()
    #app.run(debug=True)
    #results_istyle = scrape(CONFIG_ISTYLE, XPATH_PRODUCT_NAME_ISTYLE, XPATH_PRODUCT_PRICE_ISTYLE, XPATH_COOKIES_BUTTON_ISTYLE)
    #result_alza = scrape(CONFIG_ALZA, XPATH_PRODUCT_NAME_ALZA, XPATH_PRODUCT_PRICE_ALZA)
    #print(results_istyle)
    #print(result_alza)
 