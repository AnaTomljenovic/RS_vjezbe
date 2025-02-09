# Osnovna slika
FROM python:3.12.7

# Postavljanje radnog direktorija
WORKDIR /app

# Kopiranje lokalnih datoteka u radni direktorij
COPY . /app

# Instalacija potrebnih paketa
RUN pip install fastapi uvicorn

# Izlaganje porta
EXPOSE 3500

# Pokretanje aplikacije
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3500"]