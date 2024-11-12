from fastapi import APIRouter, HTTPException
from typing import List
from models.classSchedule import ClassSchedule
from repositories.classSchedule import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/classSchedule", response_model=ClassSchedule)
def create(body: ClassSchedule):
    return repoCreate(body)

@router.get("/classSchedule", response_model=List[ClassSchedule])
def readAll():
    return repoReadAll()

@router.get("/classSchedule/{id}", response_model=ClassSchedule)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/classSchedule/{id}", response_model=ClassSchedule)
def update(id: int, body: ClassSchedule):
    return repoUpdate(id, body)

@router.delete("/classSchedule/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

