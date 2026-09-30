# src\routes\review_routes.py

from fastapi import APIRouter,Depends
from src.interface.review_create_interface import ReviewCreate
from sqlmodel import Session,select
from src.db.engine import get_session
from src.models.model import Review
from src.utils.api_response import ReviewResponse
from src.utils.exception import InvalidReviewError


router = APIRouter( prefix = "/review" , tags = ["/review"])

# POST localhost:8000/reviews
@router.post("/", response_model = Review)
def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session) ):

    data_dic = Review.model_validate(review)

    session.add(data_dic) # Session mein object add karta hai Yani Database me insert krta hay
    session.commit() # Changes database mein save karta hai
    session.refresh(data_dic) # Database se latest values object mein load karta hai

    return data_dic


    # play_name: str 
    # review_name : str
    # rating:int = Field(ge= 1,le=5)
    # comment:str

# GET localhost:8000/reviews
@router.get("/", response_model = ReviewResponse)
def list_reviews(play_name: str | None = None,session: Session = Depends(get_session)):

  
    statement = select(Review).where(Review.play_name == play_name) # To select all the reviews from the Review table

    if play_name :
        statement = select(Review).where(Review.play_name == play_name)
    else:
        statement = select(Review) # To select all the reviews from the Review table

    result = session.exec(statement) # To Execute the statement and get the result
    reviews = result.all() # To Extract aal entries of the reviews from the Review table

    if not reviews:
        raise InvalidReviewError(404, play_name or "", f"No reviews found for play '{play_name}'")
    
    return ReviewResponse(count = len(reviews), items = list(reviews))