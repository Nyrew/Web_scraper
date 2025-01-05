from sqlalchemy.orm import sessionmaker
from .models import Product
from .database import engine


def check():
    # Vytvoření session
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    # Kontrola struktury
    from sqlalchemy.inspection import inspect
    columns = [column.name for column in inspect(Product).columns]
    return print("Sloupce v tabulce product:", columns)

if __name__ == "__main__":
    check()


