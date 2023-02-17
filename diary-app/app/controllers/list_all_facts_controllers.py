from fastapi import APIRouter
from database.database import database

router = APIRouter()


@router.get("/")
async def list_all_facts(db=database):
    if len(db) == 0:
        response_body = {"message": "Database is empty"}
    else:
        response_body = db
    return response_body
