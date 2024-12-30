#URL_ISTYLE = "https://istyle.cz/mac/macbook-air.html"

URL_ISTYLE = [
"https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html",
"https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-24gb-512gb-ssd-cz-vesmirne-sedy.html",
"https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-256gb-ssd-cz-vesmirne-sedy.html"
]

#URL_ALZA = "https://www.alza.cz/macbook-air-m3/18908346.htm"

URL_ALZA = [
 "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=10931503",
 "https://www.alza.cz/macbook-air-15-m3-cz-2024-vesmirne-sedy-d10866091.htm",
 "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=12283509",
 "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=10931532,"
]

# XPATH_PRODUCT_ITEM_ISTYLE = '//div[contains(@class, "ais-hits--item")]'
# XPATH_PRODUCT_ITEM_ALZA = '//div[contains(@class, "box browsingitem js-box canBuy inStockAvailability")]'
XPATH_PRODUCT_NAME_ISTYLE = '//div[@class="page-title-wrapper product"]'
XPATH_PRODUCT_NAME_ALZA = '//div[@class="nameextc"]//span'

XPATH_PRODUCT_PRICE_ISTYLE = './/div[@class="special-price"]'
XPATH_PRODUCT_PRICE_ALZA = '//div[@class="price-detail__price-box-wrapper js-price-detail__main-price-box-wrapper"]//span[@class="price-box__price"]'

XPATH_COOKIES_BUTTON_ISTYLE = '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'