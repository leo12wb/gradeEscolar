from fastapi import APIRouter, HTTPException
from typing import List
from models.auxWeekSchedule import AuxWeekSchedule
from repositories.auxWeekSchedule import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/auxWeekSchedule", response_model=AuxWeekSchedule)
def create(body: AuxWeekSchedule):
    return repoCreate(body)

@router.get("/auxWeekSchedule", response_model=List[AuxWeekSchedule])
def readAll():
    return repoReadAll()

@router.get("/auxWeekSchedule/{id}", response_model=AuxWeekSchedule)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/auxWeekSchedule/{id}", response_model=AuxWeekSchedule)
def update(id: int, body: AuxWeekSchedule):
    return repoUpdate(id, body)

@router.delete("/auxWeekSchedule/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

