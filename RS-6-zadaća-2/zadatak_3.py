from pydantic import BaseModel
from typing import List, TypedDict

class StolInfo(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: int = Field(..., description="Identifikator jela")
    naziv: str = Field(..., description="Naziv jela")
    cijena: float = Field(..., ge=0.0, description="Cijena jela ne smije biti negativna")

class RestaurantOrder(BaseModel):
    id: int = Field(..., description="Identifikator narudžbe")
    ime_kupca: str = Field(..., description="Ime kupca")
    stol_info: StolInfo = Field(..., description="Informacije o stolu")
    jela: List[Jelo] = Field(..., description="Lista jela")
    ukupna_cijena: float = Field(..., ge=0.0, description="Ukupna cijena ne smije biti negativna")
