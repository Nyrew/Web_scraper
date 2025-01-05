# Používáme oficiální Python image
FROM python:3.10-slim

# Nastavíme pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujeme všechny soubory projektu do kontejneru
COPY . .

# Nainstalujeme potřebné závislosti
RUN pip install --no-cache-dir -r requirements.txt

# Instalace Chrome a ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && apt-get clean

# Nastavení environment variable pro Chrome
ENV CHROMIUM_PATH=/usr/bin/chromium

# Nastavení prostředí pro headless režim
ENV DISPLAY=:99

# Zvolíme příkaz pro spuštění aplikace
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
