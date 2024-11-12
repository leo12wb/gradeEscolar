from pydantic import BaseModel

from typing import List,Optional

class SchoolGrid(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    schoolId: Optional[int] = None
    segmentId: Optional[int] = None
    serieId: Optional[int] = None
    classId: Optional[int] = None
    status: str 
