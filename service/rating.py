from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():
    
    def __init__(self,db) -> None:
        self.db = db
        
    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result
    
    
    def get_movie(self,movie_id :int):
        result = self.db.query(RatingModel).filter(RatingModel.movie_id == movie_id).first()
        return result
    
    