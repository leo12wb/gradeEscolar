from fastapi import APIRouter, HTTPException
from typing import List
from models.dayOfTheWeek import DayOfTheWeek
from repositories.dayOfTheWeek import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/schoolGrid", response_model=DayOfTheWeek)
def create(body: DayOfTheWeek):
    return repoCreate(body)

@router.get("/dayOfTheWeek", response_model=List[DayOfTheWeek])
def readAll():
    return repoReadAll()

@router.get("/dayOfTheWeek/{id}", response_model=DayOfTheWeek)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/dayOfTheWeek/{id}", response_model=DayOfTheWeek)
def update(id: int, body: DayOfTheWeek):
    return repoUpdate(id, body)

@router.delete("/dayOfTheWeek/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

