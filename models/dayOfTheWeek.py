from pydantic import BaseModel

from datetime import date
from typing import Optional

class DayOfTheWeek(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    week: Optional[str] = None
    abbreviation: Optional[str] = None
    ordem: Optional[int] = None
    status: str 