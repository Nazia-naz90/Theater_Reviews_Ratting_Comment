# model.py

from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import datetime, timezone

# Table ka structure (schema)
class Review(SQLModel, table= True):
    id: Optional[int]=  Field(default=None,primary_key=True)
    play_name : str = Field(index=True)
    review_name : str
    rating: int = Field(ge=1 ,le=5) 
    comment:str
    created_at: datetime = Field(default_factory=lambda:datetime.now(timezone.utc))







# # (Response Body structure)
# class ReviewRead():
#     id:int
#     play_name: str 
#     review_name : str
#     rating:int = Field(ge= 1,le=5)
#     comment:str
#     created_at : datetime


