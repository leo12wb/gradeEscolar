from pydantic import BaseModel

from datetime import date
from typing import Optional

class SchoolGridWeekHour(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    schoolGridId: Optional[int] = None
    auxGridDisciplineId: Optional[int] = None
    status: str 