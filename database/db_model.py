from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///products.db')

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    shop = Column(String(50), nullable=False)
    product_name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    url = Column(String(255), nullable=False)
    ram = Column(String(20))
    gpu = Column(String(50))
    ssd = Column(String(20))
    date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product(shop='{self.shop}', name='{self.product_name}', price={self.price})>"