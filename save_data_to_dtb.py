from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database.db_model import engine, Product, Base

def save_product_data(scraped_data: list) -> None:
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        price_text = scraped_data['price']  
        price = float(price_text.replace(',-', '').replace(' ', '').replace('Kč', ''))
        
        product = Product(
            shop=scraped_data['shop'],
            product_name=scraped_data['product_name'],
            price=price,
            url=scraped_data['url'],
            ram=scraped_data['RAM'],
            gpu=scraped_data['GPU'],
            ssd=scraped_data['SSD']
        )
        
        session.add(product)
        session.commit()
        
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_product_history(product_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Získání historie cen konkrétního produktu
        history = session.query(Product).filter(
            Product.product_name.like(f"%{product_name}%")
        ).order_by(Product.date_scraped.desc()).all()
        
        return history
    finally:
        session.close()

def get_latest_prices():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Získání nejnovějších cen všech produktů
        latest = session.query(Product).order_by(
            Product.date_scraped.desc()
        ).limit(7).all()
        
        return latest
    finally:
        session.close()

def get_all_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        latest = session.query(Product).all()
        return latest
    finally:
        session.close()
