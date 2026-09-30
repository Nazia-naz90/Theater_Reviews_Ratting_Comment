# src\interface\review_create_interface.py

from sqlmodel import SQLModel, Field


# Validation class (Request Body validation)
class ReviewCreate(SQLModel):
    play_name: str 
    review_name : str
    rating:int = Field(ge= 1,le=5)
    comment:str