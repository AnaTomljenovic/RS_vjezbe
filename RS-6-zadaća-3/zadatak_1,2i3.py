from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 1. zadatak
class NoviAutomobil(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class AutomobilSaPDV(NoviAutomobil):
    id: int
    cijena_pdv: float

automobili: List[AutomobilSaPDV] = [
    AutomobilSaPDV(id=1, marka="Toyota", model="Corolla", godina_proizvodnje=2020, cijena=20000, boja="crvena", cijena_pdv=25000),
    AutomobilSaPDV(id=2, marka="Honda", model="Civic", godina_proizvodnje=2018, cijena=18000, boja="plava", cijena_pdv=22500)
]

@app.get("/automobili/{id}", response_model=AutomobilSaPDV)
def dohvati_automobil(id: int):
    for auto in automobili:
        if auto.id == id:
            return auto
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")

# 2. zadatak
@app.get("/automobili", response_model=List[AutomobilSaPDV])
def filtriraj_automobile(
    min_cijena: float = Query(0, ge=0, description="Minimalna cijena"),
    max_cijena: float = Query(100000, ge=0, description="Maksimalna cijena"),
    min_godina: int = Query(1960, ge=1960, description="Minimalna godina proizvodnje"),
    max_godina: int = Query(2023, ge=1960, description="Maksimalna godina proizvodnje")
):
    if min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena mora biti manja od maksimalne cijene")
    if min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina mora biti manja od maksimalne godine")
    
    return [
        auto for auto in automobili
        if min_cijena <= auto.cijena <= max_cijena and min_godina <= auto.godina_proizvodnje <= max_godina
    ]

# 3. zadatak
@app.post("/automobili", response_model=AutomobilSaPDV)
def dodaj_automobil(novi_auto: NoviAutomobil):
    novi_id = len(automobili) + 1
    for auto in automobili:
        if auto.marka == novi_auto.marka and auto.model == novi_auto.model and auto.godina_proizvodnje == novi_auto.godina_proizvodnje:
            raise HTTPException(status_code=400, detail="Automobil već postoji")
    
    cijena_pdv = novi_auto.cijena * 1.25
    auto_s_pdv = AutomobilSaPDV(id=novi_id, cijena_pdv=cijena_pdv, **novi_auto.dict())
    automobili.append(auto_s_pdv)
    return auto_s_pdv
