from pydantic import BaseModel, Field
from datetime import datetime

class Izdavac(BaseModel):
    naziv: str = Field(..., description="Naziv izdavača")
    adresa: str = Field(..., description="Adresa izdavača")

class Knjiga(BaseModel):
    naslov: str = Field(..., description="Naslov knjige")
    ime_autora: str = Field(..., description="Ime autora knjige")
    prezime_autora: str = Field(..., description="Prezime autora knjige")
    godina_izdavanja: int = Field(default_factory=lambda: datetime.now().year, description="Godina izdavanja")
    broj_stranica: int = Field(..., description="Broj stranica knjige", gt=0)
    izdavac: Izdavac = Field(..., description="Podaci o izdavaču")
