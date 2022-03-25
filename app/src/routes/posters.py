from fastapi import APIRouter, Depends
from config.db import conn
from src.models.posters import posters
from src.schemas.posters import Poster
from typing import List, Union
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select, and_
import json

router = APIRouter(
    prefix="/posters",
    tags=["posters"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "",
    response_model=List[Poster],
    description="Get a list of all posters",
)
def get_posters():
    return conn.execute(posters.select()).fetchall()

@router.get(
    "/{id}",
    response_model=Poster,
    description="Get a single Poster by Id",
)
def get_poster(id: str):
    return conn.execute(posters.select().where(posters.c.id == id)).first()

@router.get(
    "/{id_media}/{moment}",
    description="Get a single Poster by Id and Day moment [morning/daily/evening]",
)
def get_moment_poster(id_media: str, moment: str):
    if moment == 'morning':
        return conn.execute(select(posters.c.id, posters.c.morning_poster).where(posters.c.id_media == id_media)).first()
    if moment == 'daily':
        return conn.execute(select(posters.c.id, posters.c.daily_poster).where(posters.c.id_media == id_media)).first()
    if moment == 'evening':
        return conn.execute(select(posters.c.id, posters.c.evening_poster).where(posters.c.id_media == id_media)).first()

@router.post(
    "",
    response_model=Poster, 
    description="Create a new Poster")
def create_poster(poster: Poster):
    new_poster = {
        "id_media": poster.id_media, 
        "morning_poster": poster.morning_poster,
        "daily_poster": poster.daily_poster,
        "evening_poster": poster.evening_poster,
        }
    result = conn.execute(posters.insert().values(new_poster))
    return conn.execute(posters.select().where(posters.c.id == result.lastrowid)).first()

@router.put(
    "/{id}",
    response_model=Poster, 
    description="Update a Poster by Id"
)
def update_poster(poster: Poster, id: int):
    conn.execute(
        posters.update()
        .values(id_media=poster.id_media, 
                morning_poster=poster.morning_poster,
                daily_poster=poster.daily_poster,
                evening_poster=poster.evening_poster)
        .where(posters.c.id == id)
    )
    return conn.execute(posters.select().where(posters.c.id == id)).first()

@router.delete(
    "/{id}",
    status_code=HTTP_204_NO_CONTENT
)
def delete_poster(id: int):
    conn.execute(posters.delete().where(posters.c.id == id))
    return conn.execute(posters.select().where(posters.c.id == id)).first()
