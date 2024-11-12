from pydantic import BaseModel

from datetime import date
from typing import Optional

class ClassSchedule(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    ordem: Optional[int] = None
    start_date: date = None
    end_date: date = None
    status: str 