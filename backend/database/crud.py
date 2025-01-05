from sqlalchemy import delete, func
from sqlalchemy.orm import Session
from datetime import datetime
from database.models import Product

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
    filtered_data = (
        db.query(Product)
        .filter(Product.id >= 1, Product.id <= 7)
        .all()
    )

    latest_data = {}
    for product in filtered_data:
        if product.id not in latest_data or product.date > latest_data[product.id].date:
            latest_data[product.id] = product
            
    alza_data = []
    istyle_data = []

    for product in latest_data.values():
        product_dict = {
            "id": product.id,
            "product_name": product.product_name,
            "price": product.price,
            "ram": product.ram,
            "ssd": product.ssd
        }
        if product.shop == "alza":
            alza_data.append(product_dict)
        elif product.shop == "istyle":
            istyle_data.append(product_dict)

    return {"alza": alza_data, "istyle": istyle_data}

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
