# Koristimo Python 3.12
FROM python:3.12.7

# Postavljanje radnog direktorija
WORKDIR /app

# Kopiranje potrebnih datoteka
COPY authapi.py /app/authapi.py

# Instalacija potrebnih paketa
RUN pip install aiohttp

# Pokretanje aplikacije
CMD ["python", "authapi.py"]

EXPOSE 9000
