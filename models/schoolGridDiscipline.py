from pydantic import BaseModel

from typing import Optional

class SchoolGridDiscipline(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    schoolGridTeacherId: Optional[int] = None
    disciplineId: Optional[int] = None
    status: str 