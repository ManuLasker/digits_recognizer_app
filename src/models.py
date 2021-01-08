from typing import Optional
from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prob: Optional[str] = None
    class_name: Optional[int] = None

class ImageRequest(BaseModel):
    image_data: str