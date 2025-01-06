from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from backend.database.models import Product

# Connection string k vaší databázi
DATABASE_URL = "postgresql://products_p1zv_user:LlARnqsJ8rx9FoYdWoacpJi1gMmI6KE2@dpg-ctt2s9tumphs73fr35lg-a.frankfurt-postgres.render.com/products_p1zv"

# Nastavení připojení k databázi
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Přidání jednoho záznamu
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
        session.add(new_product)
        session.commit()
        print("New product added successfully!")
    except Exception as e:
        print("Error:", e)
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    add_product()