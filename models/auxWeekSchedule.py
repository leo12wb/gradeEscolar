from pydantic import BaseModel

from typing import Optional

class AuxWeekSchedule(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    schoolGridWeekHourId: Optional[int] = None
    dayOfTheWeekId: Optional[int] = None
    classScheduleId: Optional[int] = None
    status: str 