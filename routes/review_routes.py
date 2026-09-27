from fastapi import APIRouter,Depends
from interface.review_create_interface import ReviewCreate
from sqlmodel import Session
from engine import get_session
from model import Review

router = APIRouter( prefix = "/review" , tags = ["/review"])

@router.post("/", response_model = Review)
def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session) ):

    data_dic = Review.model_validate(review)

    session.add(data_dic) # Database me insert kr diya
    session.commit() # Save into Database
    session.refresh(data_dic) # 

    return data_dic


    # play_name: str 
    # review_name : str
    # rating:int = Field(ge= 1,le=5)
    # comment:str

