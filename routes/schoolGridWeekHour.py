from fastapi import APIRouter, HTTPException
from typing import List
from models.schoolGridWeekHour import SchoolGridWeekHour
from repositories.schoolGridWeekHour import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/schoolGridWeekHour", response_model=SchoolGridWeekHour)
def create(body: SchoolGridWeekHour):
    return repoCreate(body)

@router.get("/schoolGridWeekHour", response_model=List[SchoolGridWeekHour])
def readAll():
    return repoReadAll()

@router.get("/schoolGridWeekHour/{id}", response_model=SchoolGridWeekHour)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/schoolGridWeekHour/{id}", response_model=SchoolGridWeekHour)
def update(id: int, body: SchoolGridWeekHour):
    return repoUpdate(id, body)

@router.delete("/schoolGridWeekHour/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

