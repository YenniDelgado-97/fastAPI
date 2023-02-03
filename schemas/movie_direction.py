from pydantic import BaseModel

class Movie_direction(BaseModel):
    movie_id : int
    dir_id: int
    
    class config:
        schema_extra = {
            "example":{
                "movie:id":4,
                "dir_id": 5,
            }
        }