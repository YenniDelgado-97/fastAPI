from fastapi import APIRouter,Path,Query
from models.director import Director
from typing import List
from config.database import Session
from service.director import DirectorService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.director import Director
from models.director import Director as DirectorModel

director_router = APIRouter()


@director_router.get('/director', tags=['director'], response_model= List[Director], status_code=200)
def get_directors() -> Director:
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/{id}',tags=['director'],response_model=Director)
def get_director_by_id(id:int = Path(ge=0,le=2000)):
    db = Session()
    result = DirectorService(db).get_director_by_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found director with that id"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/',tags=['director'],response_model=List[Director],status_code=200)
def get_director_by_fname(fname:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(DirectorModel).filter(DirectorModel.fname == fname).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found director with that id"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.post('/director',tags=['director'],status_code=201,response_model=dict)
def create_director(director:Director)->dict:
    db = Session()
    DirectorService(db).create_Director(director)
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})

