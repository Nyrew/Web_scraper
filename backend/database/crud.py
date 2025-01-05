from sqlalchemy import delete, func
from sqlalchemy.orm import Session
from datetime import datetime
from models import Product

def save_scraped_data(db: Session, scraped_data_multiple: dict):

    for scraped_data in scraped_data_multiple:
        if check_product_exists(db, scraped_data['product_id'], datetime.now()):
            print("Duplciity")
            continue
        price_text = scraped_data['price']  
        price = float(price_text.replace(',-', '').replace(' ', '').replace('Kč', ''))
        
        db_item = Product(
                shop=scraped_data['shop'],
                product_name=scraped_data['product_name'],
                product_id=scraped_data['product_id'],
                price=price,
                url=scraped_data['url'],
                ram=scraped_data['RAM'],
                gpu=scraped_data['GPU'],
                ssd=scraped_data['SSD'],
                date=datetime.now()
        )
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    return db_item

def get_all_data(db: Session):
    data = db.query(Product).all()
    # return data
    return [product.__dict__ for product in data]

def delete_all_products(db: Session):
    stmt = delete(Product)
    db.execute(stmt)
    db.commit()
    print("Deleted")
       
def delete_product_by_product_criteria(db: Session, product_id: int, date: datetime):
    stmt = delete(Product).where(
        Product.product_id == product_id,
        Product.date < date
    )
    db.execute(stmt)
    db.commit()
    print("Deleted")
    
def check_product_exists(db: Session, product_id: int, date: datetime) -> bool:    
    check_date = date.date()
    
    result = db.query(Product).filter(
        Product.product_id == product_id,
        func.date(Product.date) == check_date
    ).first()
    
    return result is not None