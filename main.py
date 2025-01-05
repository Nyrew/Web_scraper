import psycopg2

# Connection string k vaší databázi
DATABASE_URL = "postgresql://products_p1zv_user:LlARnqsJ8rx9FoYdWoacpJi1gMmI6KE2@dpg-ctt2s9tumphs73fr35lg-a.frankfurt-postgres.render.com/products_p1zv"

def fetch_all_data():
    try:
        # Připojení k databázi
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # SQL dotaz pro výběr všech dat
        query = "SELECT * FROM product;"  # Přizpůsobte název tabulky
        cursor.execute(query)

        # Načtení všech řádků
        rows = cursor.fetchall()

        # Vypsání dat do konzole
        for row in rows:
            print(row)

        # Zavření kurzoru a spojení
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    fetch_all_data()
