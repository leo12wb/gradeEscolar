from fastapi import APIRouter, HTTPException
from typing import List
from models.authToken import AuthToken
from repositories.authToken import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/authToken", response_model=AuthToken)
def create(body: AuthToken):
    return repoCreate(body)

@router.get("/authToken", response_model=List[AuthToken])
def readAll():
    return repoReadAll()

@router.get("/authToken/{id}", response_model=AuthToken)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/authToken/{id}", response_model=AuthToken)
def update(id: int, body: AuthToken):
    return repoUpdate(id, body)

@router.delete("/authToken/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

