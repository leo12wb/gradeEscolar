from pydantic import BaseModel

from typing import Optional

class AuxGridWeekHour(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    schoolGridWeekHourId: Optional[int] = None
    auxWeekScheduleId: Optional[int] = None
    status: str 