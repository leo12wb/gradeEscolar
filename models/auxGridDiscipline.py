from pydantic import BaseModel

from typing import Optional

class AuxGridDiscipline(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    schoolGridId: Optional[int] = None
    schoolGridDisciplineId: Optional[int] = None
    status: str 