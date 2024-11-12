from fastapi import APIRouter, HTTPException
from typing import List
from models.schoolGrid import SchoolGrid
from repositories.schoolGrid import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    readOneFull as repoReadOneFull,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/schoolGrid", response_model=SchoolGrid)
def create(body: SchoolGrid):
    return repoCreate(body)

@router.get("/schoolGrid", response_model=List[object])
def readAll():
    return repoReadAll()

@router.get("/schoolGrid/{id}", response_model=object)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.get("/schoolGrid/{id}/full", response_model=object)
def read(id: int):
    res = repoReadOneFull(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/schoolGrid/{id}", response_model=SchoolGrid)
def update(id: int, body: SchoolGrid):
    return repoUpdate(id, body)

@router.delete("/schoolGrid/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

