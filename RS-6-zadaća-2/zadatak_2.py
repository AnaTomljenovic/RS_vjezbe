from pydantic import BaseModel, EmailStr
from typing import List, Literal

class Admin(BaseModel):
    ime: str = Field(..., description="Ime administratora")
    prezime: str = Field(..., description="Prezime administratora")
    korisnicko_ime: str = Field(..., description="Korisničko ime administratora")
    email: EmailStr = Field(..., description="Email adresa administratora")
    ovlasti: List[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = Field(default_factory=list, description="Lista ovlasti administratora")
