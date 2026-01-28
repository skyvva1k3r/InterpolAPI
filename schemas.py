from pydantic import BaseModel, Field
from typing import Optional

class Search(BaseModel):
    level: Optional[str] = Field(default="", pattern="^[YR]?$")
    forename: Optional[str] = ""
    name: Optional[str] = ""
    nation: Optional[str] = Field(default="", max_length=2)
    ageMax: Optional[int] = Field(default=120, ge=0, le=120)
    ageMin: Optional[int] = Field(default=0, ge=0, le=120)
    sex: Optional[str] = Field(default="", pattern="^[MFU]?$")
    warrantCountry: Optional[str] = Field(default="", max_length=2)
