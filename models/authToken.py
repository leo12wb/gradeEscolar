from pydantic import BaseModel

from typing import Optional

class AuthToken(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    token: str 
    appId: Optional[int] = None
    status: str 