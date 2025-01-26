from pydantic import BaseModel, Field
from datetime import datetime
from typing import Tuple

class CCTVFrame(BaseModel):
    id: int = Field(..., description="Jedinstveni identifikator slike")
    vrijeme_snimanja: datetime = Field(..., description="Vrijeme kada je slika snimljena")
    koordinate: Tuple[float, float] = Field(default=(0.0, 0.0), description="Koordinate x i y")
