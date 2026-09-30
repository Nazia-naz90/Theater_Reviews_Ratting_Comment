# src\utils\api_response.py

from typing import List
from sqlmodel import SQLModel
from src.models.model import Review



class ReviewResponse(SQLModel):
    status: str = "success"
    count: int
    items: List[Review]