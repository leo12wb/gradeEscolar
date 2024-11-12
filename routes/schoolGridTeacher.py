from fastapi import APIRouter, HTTPException
from typing import List
from models.schoolGridTeacher import SchoolGridTeacher
from repositories.schoolGridTeacher import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/schoolGridTeacher", response_model=SchoolGridTeacher)
def create(body: SchoolGridTeacher):
    return repoCreate(body)

@router.get("/schoolGridTeacher", response_model=List[SchoolGridTeacher])
def readAll():
    return repoReadAll()

@router.get("/schoolGridTeacher/{id}", response_model=SchoolGridTeacher)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/schoolGridTeacher/{id}", response_model=SchoolGridTeacher)
def update(id: int, body: SchoolGridTeacher):
    return repoUpdate(id, body)

@router.delete("/schoolGridTeacher/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

