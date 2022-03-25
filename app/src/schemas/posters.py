from typing import Optional
from pydantic import BaseModel

class Poster(BaseModel):
    id: Optional[int]
    id_media: int
    morning_poster: str
    daily_poster: str
    evening_poster: str
