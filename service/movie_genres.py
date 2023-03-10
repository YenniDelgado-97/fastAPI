from models.movie_genres import MoviesGenres as MoviesGenresModel
from schemas.movie_genres import Movie_genres


class MovieGenresService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movie_genres(self):
        result = self.db.query(MoviesGenresModel).all()
        return result
    
    def get_movie_genres(self, movie_id:int):
        result= self.db.query(MoviesGenresModel).filter(MoviesGenresModel.movie_id == movie_id).first()
        return result
    
    def get_movie_genres_by_gen_id(self, gen_id:int):
        result = self.db.query(MoviesGenresModel).filter(MoviesGenresModel.gen_id == gen_id).all()
        return result
    
    def create_movie_genres(self, movie_genres:Movie_genres):
        new_movies_genres = MoviesGenresModel(
        movie_id = movie_genres.movie_id,
        gen_id = movie_genres.gen_id
        )
        self.db.add(new_movies_genres)
        self.db.commit()
        return 
            
        
    def update_movie_genres(self,movie_id:int, data:Movie_genres):
        movie_genres = self.db.query(Movie_genres).filter(Movie_genres.movie_id== movie_id).first()
        movie_genres.gen_id = data.gen_id
        self.db.commit()
        return
    
    def delete_movie_genres(self,gen_id:int):
        self.db.query(Movie_genres).filter(Movie_genres.gen_id == gen_id).delete()
        self.db.commit()
        return
    
    