from fastapi import APIRouter, HTTPException
from typing import List
from models.schoolGridDiscipline import SchoolGridDiscipline
from repositories.schoolGridDiscipline import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/schoolGridDiscipline", response_model=SchoolGridDiscipline)
def create(body: SchoolGridDiscipline):
    return repoCreate(body)

@router.get("/schoolGridDiscipline", response_model=List[SchoolGridDiscipline])
def readAll():
    return repoReadAll()

@router.get("/schoolGridDiscipline/{id}", response_model=SchoolGridDiscipline)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/schoolGridDiscipline/{id}", response_model=SchoolGridDiscipline)
def update(id: int, body: SchoolGridDiscipline):
    return repoUpdate(id, body)

@router.delete("/schoolGridDiscipline/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

