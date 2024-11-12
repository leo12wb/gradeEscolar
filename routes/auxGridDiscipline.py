from fastapi import APIRouter, HTTPException
from typing import List
from models.auxGridDiscipline import AuxGridDiscipline
from repositories.auxGridDiscipline import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/auxGridDiscipline", response_model=AuxGridDiscipline)
def create(body: AuxGridDiscipline):
    return repoCreate(body)

@router.get("/auxGridDiscipline", response_model=List[AuxGridDiscipline])
def readAll():
    return repoReadAll()

@router.get("/auxGridDiscipline/{id}", response_model=AuxGridDiscipline)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/auxGridDiscipline/{id}", response_model=AuxGridDiscipline)
def update(id: int, body: AuxGridDiscipline):
    return repoUpdate(id, body)

@router.delete("/auxGridDiscipline/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

