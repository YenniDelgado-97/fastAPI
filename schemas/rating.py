from pydantic import BaseModel

class Rating(BaseModel):
    
    movie_id:int
    rev_id:int
    rev_starts:int
    num_o_rating:int
    
    class Config:
        schema_extra = {
            "example":{
                'movie_id': 3,
                'rev_id':6,
                'rev_starts': 8,
                'num_o_rating':10,
            }
        }