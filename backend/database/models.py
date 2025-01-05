from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True,  autoincrement=True)
    shop = Column(String(50), nullable=False)
    product_name = Column(String(255), nullable=False)
    product_id = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    url = Column(String(255), nullable=False)
    ram = Column(String(20))
    gpu = Column(String(50))
    ssd = Column(String(20))
    date = Column(DateTime)