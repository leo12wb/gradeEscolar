from pydantic import BaseModel

from datetime import date
from typing import Optional

class SchoolGridTeacher(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    useId: Optional[int] = None
    status: str 